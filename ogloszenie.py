from dataclasses import dataclass
from typing import Optional, List, Any
from enum import Enum
from datetime import datetime
from uuid import UUID


@dataclass
class AdCategory:
    id: int
    name: str
    typename: str
    number: Optional[int] = None
    type: Optional[str] = None
    code: Optional[str] = None


class AdditionalInformationTypename(Enum):
    AdditionalInfo = "AdditionalInfo"
    FeatureGroup = "FeatureGroup"


class Unit(Enum):
    empty = ""
    m = "m²"


@dataclass
class AdditionalInformation:
    label: str
    values: List[str]
    typename: AdditionalInformationTypename
    unit: Optional[Unit] = None


@dataclass
class Breadcrumb:
    label: str
    locative: str
    url: str
    typename: str


@dataclass
class Name:
    locale: str
    value: str
    typename: str


@dataclass
class Category:
    id: int
    name: List[Name]
    typename: str


class PriceCurrency(Enum):
    PLN = "PLN"
    empty = ""


class CharacteristicTypename(Enum):
    Characteristic = "Characteristic"


@dataclass
class Characteristic:
    key: str
    value: str
    label: str
    localizedValue: str
    currency: PriceCurrency
    suffix: str
    typename: CharacteristicTypename


@dataclass
class ContactDetails:
    name: str
    type: str
    phones: List[str]
    imageUrl: str


@dataclass
class Image:
    thumbnail: str
    small: str
    medium: str
    large: str
    typename: str


@dataclass
class Links:
    localPlanUrl: str
    videoUrl: str
    view3dUrl: str
    walkaroundUrl: str
    typename: str


@dataclass
class Address:
    street: AdCategory
    subdistrict: None
    district: AdCategory
    city: AdCategory
    municipality: None
    county: AdCategory
    province: AdCategory
    postalCode: None
    typename: str


@dataclass
class Coordinates:
    latitude: float
    longitude: float
    typename: str


@dataclass
class MapDetails:
    radius: int
    zoom: int
    typename: str


@dataclass
class LocationElement:
    id: str
    locationLevel: str
    name: str
    fullName: str
    fullNameItems: List[str]
    parentIds: List[str]
    typename: str


@dataclass
class ReverseGeocoding:
    locations: List[LocationElement]
    typename: str


@dataclass
class AdLocation:
    id: None
    coordinates: Coordinates
    mapDetails: MapDetails
    address: Address
    reverseGeocoding: ReverseGeocoding
    typename: str


@dataclass
class OpenDay:
    date: None
    timeFrom: None
    timeTo: None
    typename: str


@dataclass
class Owner:
    id: int
    name: str
    type: str
    phones: List[str]
    imageUrl: str
    contacts: List[Any]
    typename: str


@dataclass
class PaginatedUnits:
    items: None
    isPriceHidden: None
    pagination: None
    facets: None
    typename: str


@dataclass
class Area:
    value: float
    unit: str
    typename: str


@dataclass
class BuildingProperties:
    year: int
    type: str
    material: None
    windows: List[str]
    heating: str
    numberOfFloors: int
    conveniences: List[str]
    security: List[str]
    typename: str


@dataclass
class Properties:
    equipment: List[Any]
    areas: List[str]
    floor: str
    kitchen: None
    parking: List[Any]
    numberOfRooms: int
    rooms: List[Any]
    type: None
    windowsOrientation: List[Any]
    typename: str


@dataclass
class Property:
    id: None
    type: str
    rent: None
    costs: List[Any]
    condition: str
    properties: Properties
    buildingProperties: BuildingProperties
    ownership: str
    area: Area
    typename: str


@dataclass
class SEO:
    title: str
    description: str
    typename: str


@dataclass
class Target:
    Area: str
    AreaRange: List[Any]
    Buildyear: int
    Buildingfloorsnum: int
    Buildingownership: List[str]
    Buildingtype: List[str]
    City: str
    Cityid: int
    Constructionstatus: List[str]
    Country: str
    Extrastypes: List[str]
    Floorno: List[str]
    Heating: List[str]
    Id: int
    MarketType: str
    Mediatypes: List[str]
    ObidoAdvert: str
    OfferType: str
    Photo: str
    Price: int
    PriceRange: List[str]
    Priceperm: int
    ProperType: str
    Province: str
    RegularUser: str
    Roomsnum: List[int]
    Securitytypes: List[str]
    Subregion: str
    Title: str
    Windowstype: List[str]
    categoryId: int
    env: str
    hidePrice: int
    sellerid: int
    usertype: str


@dataclass
class Price:
    value: int
    unit: PriceCurrency
    typename: str


@dataclass
class UserAdvert:
    adId: int
    url: str
    image: str
    roomsNum: str
    pricePerM: int
    price: Price
    netArea: str
    title: str
    typename: str


@dataclass
class Ad:
    id: int
    market: str
    services: List[Any]
    publicId: str
    slug: str
    advertiserType: str
    advertType: str
    source: str
    createdAt: datetime
    modifiedAt: datetime
    description: str
    developmentId: int
    developmentTitle: str
    developmentUrl: str
    exclusiveOffer: bool
    externalId: str
    features: List[str]
    featuresByCategory: List[AdditionalInformation]
    featuresWithoutCategory: List[Any]
    openDay: OpenDay
    referenceId: str
    target: Target
    title: str
    topInformation: List[AdditionalInformation]
    additionalInformation: List[AdditionalInformation]
    url: str
    status: str
    adCategory: AdCategory
    category: Category
    characteristics: List[Characteristic]
    images: List[Image]
    links: Links
    location: AdLocation
    property: Property
    owner: Owner
    agency: None
    seo: SEO
    breadcrumbs: List[Breadcrumb]
    userAdverts: List[UserAdvert]
    paginatedUnits: PaginatedUnits
    specialOffer: None
    typename: str
    contactDetails: ContactDetails


@dataclass
class AdTrackingData:
    touchpointpage: str
    lat: float
    long: float
    adphoto: int
    pricecurrency: PriceCurrency
    catl1id: int
    catl1name: str
    specialoffertype: None
    adid: int
    adprice: int
    business: str
    cityid: int
    cityname: str
    market: str
    postertype: str
    surface: None
    regionid: str
    regionname: str
    subregionid: str
    sellerid: int
    obidoadvert: str


@dataclass
class Experiments:
    EUADS4564: None
    REPM844: None
    SEE1767: str
    SFS572: str
    SFS710: None
    SMR2326: None
    SEE1753: str
    SEE1754: None
    SEORE490: str


@dataclass
class FeatureFlags:
    isAdAvmModuleEnabled: bool
    isAdFinanceBannerEnabled: bool
    isAdFinanceLinkEnabled: bool
    isAdMortgageSimulatorEnabled: bool
    isAgentsSubaccountsEnabled: bool
    isBulkSchedulingEnabled: bool
    isFeaturedDevelopmentVASEnabled: bool
    isListingRentPriceEnabled: bool
    isMapEnabled: bool
    isNewApartmentsForSalePostingFormEnabled: bool
    isNewPromotePageEnabled: bool
    isOldSaveSearchQueryEnabled: bool
    shouldRolloutLocationService: bool
    isOlxAdvertPromotionEnabled: bool
    isOtodomAnalyticsEnabled: bool
    isProjectREDEnabled: bool
    isPushNotificationServiceWorkerEnabled: bool
    isPushNotificationsToggleEnabled: bool
    isSavedSearchFrequencyChangeEnabled: bool
    isVasRecommendationsEnabled: bool
    isVasSchedulingEnabled: bool
    shouldUseNewInformation: bool
    shouldUseNewProjectPage: bool
    isFinanceCheckboxEnabled: bool
    isObservedAdsPageEnabled: bool
    isNewAskAboutPriceEnabled: bool
    isHomepageVasConverted: bool
    isDevelopersPricingCardsDesignEnabled: bool
    isUnifiedBusinessInvoicesPageActive: bool
    isRegularMyAccountAdsPageEnabled: bool
    isBikPromotionEnabled: bool
    isStudioFlatCategoryEnabled: bool
    isRegularRoomCategoryMigratedToNMF: bool
    isSpecialOfferForUnitsExperimentEnabled: bool
    isRegularExtendedBundlesEnabled: bool
    isStaticInternalLinkingSectionEnabled: bool
    isRegularOlxVasesEnabled: bool
    isSpecialOfferEnabled: bool
    isBulkOlxPromotionEnabled: bool
    isRegularVasRecommendationsEnabled: bool
    isSeoAdsDescriptionEnabled: bool
    isPropertyEvaluationPageActive: bool
    isSettingsGeneralTabMigrated: bool
    isSettingsContactsTabMigrated: bool
    typename: str


@dataclass
class PageProps:
    lang: str
    sentryTraceData: str
    sentryBaggage: str
    experiments: Experiments
    id: str
    ad: Ad
    relativeUrl: str
    adTrackingData: AdTrackingData
    referer: str
    currentUser: None
    featureFlags: FeatureFlags
    laquesisResult: str
    userSessionId: UUID
    unconfirmedUserAuthToken: None
    isBotDetected: bool


@dataclass
class Props:
    pageProps: PageProps
    NSSP: bool


@dataclass
class Query:
    id: str


@dataclass
class RuntimeConfig:
    appleCognitoLoginUrl: str
    env: str
    fbCognitoLoginUrl: str
    fileUploadServiceUrl: str
    googleApiKey: str
    isOneTrustAutoDeleteEnabled: bool
    isOneTrustEnabled: bool
    isSentryEnabled: bool
    googleCognitoLoginUrl: str
    oneTrustSiteId: UUID
    ninjaEnvironment: str
    nodeEnv: str
    pushNotificationPublicKey: str
    sentryDsn: str
    sentryEnvironment: str
    sentrySampleRateClient: float
    sentryTracesSampleRateClient: int
    staticAssetsPrefix: str


@dataclass
class Ogloszenie:
    props: Props
    page: str
    query: Query
    buildId: str
    assetPrefix: str
    runtimeConfig: RuntimeConfig
    isFallback: bool
    dynamicIds: List[int]
    gssp: bool
    customServer: bool
    appGip: bool
    scriptLoader: List[Any]
