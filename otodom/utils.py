import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from geopy.geocoders import Bing

from dotenv import load_dotenv
import os

load_dotenv()


def after_dot(string: str):
    return string[string.find('.')+1:]


def history_fill(main_df: pd.DataFrame, source_df: pd.DataFrame, fill_col: str, join_col: str):
    main_df[fill_col].fillna(pd.merge(main_df, source_df, how='left', on=join_col, suffixes=(
        '', '_new'))[fill_col+'_new'], inplace=True)


def add_empty_col(df: pd.DataFrame, colname: str):
    if colname not in df.columns:
        df[colname] = np.nan


# Geolocation 45min-5k records
class Geolocator():
    def geo_bing(self, adress: str, mode='dict'):
        bing = Bing(api_key=os.environ.get("BING_MAPS"))
        adress = adress.split(', ')
        if mode == 'dict':
            query_dict = {'addressLine': adress[0],
                          'locality': adress[-2],
                          'adminDistrict': adress[-1],
                          'countryRegion': 'Poland'}
            # print('qb',query_dict)
        elif mode == 'short':
            query_dict = {'addressLine': adress[-3],
                          'locality': adress[-2],
                          'adminDistrict': adress[-1],
                          'countryRegion': 'Poland'}
        else:
            # mode string
            query_dict = adress

        data = bing.geocode(query_dict, exactly_one=True,
                            include_neighborhood=True)
        rawdict = data.raw['address']

        return (data.latitude, data.longitude, rawdict)

    def geo_nominatim(self, adress: str, county=True):

        nominatim = Nominatim(user_agent="http")

        adress = adress.split(', ')
        if county:
            query_dict = {'street': after_dot(adress[0]),
                          'city': adress[-2],
                          'county': adress[-3],
                          'state': adress[-1],
                          'country': 'pl'}
        else:
            query_dict = {'street': after_dot(adress[0]),
                          'city': adress[-2],
                          'state': adress[-1],
                          'country': 'pl'}

        data = nominatim.geocode(
            query_dict, country_codes='pl', exactly_one=True, addressdetails=True)
        try:
            ndict = data.raw['address']
            return (data.latitude, data.longitude, ndict)
        except:
            return

    def geo_nominatim_postal(self, postcode: str):

        nominatim = Nominatim(user_agent="http")
        query_dict = {'postalcode': postcode}
        data = nominatim.geocode(
            query_dict, country_codes='pl', exactly_one=True, addressdetails=True)
        ndict = data.raw['address']
        return (data.latitude, data.longitude, ndict)

    def geo_nominatim_gps(self, la, lo):
        print('gps')
        nominatim = Nominatim(user_agent="http")
        query = (la, lo)
        data = nominatim.reverse(query, exactly_one=True, addressdetails=True)
        ndict = data.raw['address']
        # print(data)
        return (data.latitude, data.longitude, ndict)

    def get_geo(self, adress):

        # try with county
        geo = self.geo_nominatim(adress, county=True)
        if geo:
            return geo
        # try without county
        geo = self.geo_nominatim(adress, county=False)
        if geo:
            return geo
        # try with bing and return to nominatim
        geo = self.geo_bing(adress)
        if geo:
            la, lo, d = geo
            # print(1,d)

            if 'postalCode' in d.keys():
                try:
                    geo = self.geo_nominatim_postal(d['postalCode'])
                except:
                    try:
                        geo = self.geo_nominatim_gps(la, lo)
                        # retain bing postal code
                        geo[2]['postalCode'] = d['postalCode']
                    except:
                        pass
            else:
                try:
                    geo = self.geo_bing(adress, mode='short')
                    _, _, d = geo
                    # print(2,d)
                    geo = self.geo_nominatim_postal(d['postalCode'])
                    # retain bing postal code
                    geo[2]['postalCode'] = d['postalCode']
                except:
                    try:
                        geo = self.geo_bing(adress, mode='string')
                        la, lo, d = geo
                        geo = self.geo_nominatim_gps(la, lo)
                        print('str')
                    except:
                        pass
            return geo

    def add_geo(self, series: pd.Series, source_col='where'):

        try:
            la, lo, d = self.get_geo(series[source_col])
            if 'neighbourhood' not in d.keys():
                if 'quarter' in d.keys():
                    d['neighbourhood'] = d['quarter']
                else:
                    d['neighbourhood'] = 'brak'
            if 'suburb' not in d.keys():
                if 'city_district' in d.keys():
                    d['suburb'] = d['city_district']
                else:
                    d['suburb'] = 'brak'
            if 'postcode' not in d.keys():
                try:
                    d['postcode'] = d['postalCode']
                except:
                    d['postcode'] = 'brak'

            series['latitude'], series['longitude'], series['neighbourhood'], series[
                'suburb'], series['postcode'] = la, lo, d['neighbourhood'], d['suburb'], d['postcode']
        except:
            print(series[source_col])
        return series

    def geolocate_empty(self, df, source_col='where'):
        # before geocoding
        # add missing columns
        for col in ['latitude', 'longitude', 'neighbourhood', 'suburb', 'postcode']:
            add_empty_col(df, col)
        # prepare known list
        without_dupli = df.drop_duplicates(source_col)
        known_without_dupli = without_dupli[without_dupli['latitude'].notna()]
        # first geocode base on already known
        for col in ['latitude', 'longitude', 'neighbourhood', 'suburb', 'postcode']:
            history_fill(df, known_without_dupli, col, source_col)

        new_without_dupli = without_dupli.loc[df['latitude'].isna(
        )][source_col].to_frame()
        print(f'{new_without_dupli.shape[0]} - records needs geocoding')
        # only new without gps remains, need geocoding
        # GEOCODING
        new_without_dupli_gps = new_without_dupli.apply(
            lambda x: self.add_geo(x, source_col), axis=1)
        # now fill based on new data
        for col in ['latitude', 'longitude', 'neighbourhood', 'suburb', 'postcode']:
            history_fill(df, new_without_dupli_gps, col, source_col)
