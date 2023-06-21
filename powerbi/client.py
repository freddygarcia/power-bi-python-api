from powerbi.datasets import Datasets
from powerbi.session import PowerBiSession
from powerbi.dashboards import Dashboards
from powerbi.groups import Groups
from powerbi.users import Users
from powerbi.template_apps import TemplateApps
from powerbi.dataflow_storage_account import DataflowStorageAccount
from powerbi.push_datasets import PushDatasets
from powerbi.imports import Imports
from powerbi.reports import Reports
from powerbi.available_features import AvailableFeatures
from powerbi.capacities import Capacities
from powerbi.pipelines import Pipelines
from powerbi.apps import Apps


class PowerBiClient:

    """
    ### Overview
    ----
    Is the main entry point to the other Power BI
    REST Services.
    """

    def __init__(self, power_bi_session: PowerBiSession):
        """Initializes the Graph Client.

        ### Parameters
        ----
        power_bi_session (PowerBiSession) :
            An instance of the `PowerBiSession` class.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> apps_service = power_bi_client.apps()
        """
        self.power_bi_session = power_bi_session

    def apps(self) -> Apps:
        """Used to access the `Apps` Services and metadata.

        ### Returns
        ---
        Apps :
            The `Apps` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> apps_service = power_bi_client.apps()
        """

        return Apps(session=self.power_bi_session)

    def dashboards(self) -> Dashboards:
        """Used to access the `Dashboards` Services and metadata.

        ### Returns
        ---
        Dashboards :
            The `Dashboards` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> dashboard_service = power_bi_client.dashboards()
        """

        return Dashboards(session=self.power_bi_session)

    def groups(self) -> Groups:
        """Used to access the `Groups` Services and metadata.

        ### Returns
        ---
        Groups :
            The `Groups` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> groups_service = power_bi_client.groups()
        """

        return Groups(session=self.power_bi_session)

    def users(self) -> Users:
        """Used to access the `Users` Services and metadata.

        ### Returns
        ---
        Users :
            The `Users` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> users_service = power_bi_client.users()
        """

        return Users(session=self.power_bi_session)

    def template_apps(self) -> TemplateApps:
        """Used to access the `TemplateApps` Services and metadata.

        ### Returns
        ---
        TemplateApps :
            The `TemplateApps` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> template_apps_service = power_bi_client.template_apps()
        """

        return TemplateApps(session=self.power_bi_session)

    def dataflow_storage_account(self) -> DataflowStorageAccount:
        """Used to access the `DataflowStorageAccount` Services and metadata.

        ### Returns
        ---
        DataflowStorageAccount :
            The `DataflowStorageAccount` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> dataflow_storage_service = power_bi_client.dataflow_storage_accounts()
        """

        return DataflowStorageAccount(session=self.power_bi_session)

    def push_datasets(self) -> PushDatasets:
        """Used to access the `PushDatasets` Services and metadata.

        ### Returns
        ---
        PushDatasets :
            The `PushDatasets` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> push_datasets_service = power_bi_client.push_datasets()
        """

        return PushDatasets(session=self.power_bi_session)

    def imports(self) -> Imports:
        """Used to access the `Imports` Services and metadata.

        ### Returns
        ---
        Imports:
            The `Imports` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> imports_service = power_bi_client.imports()
        """

        return Imports(session=self.power_bi_session)

    def reports(self) -> Reports:
        """Used to access the `Reports` Services and metadata.

        ### Returns
        ---
        Reports:
            The `Reports` services Object.

        ### Usage
        ----
            >>> power_bi_client = PowerBiClient(power_bi_session=power_bi_session)
            >>> reports_service = power_bi_client.reports()
        """

        return Reports(session=self.power_bi_session)

    def available_features(self) -> AvailableFeatures:
        """Used to access the `AvailableFeatures` Services and metadata.

        ### Returns
        ---
        AvailableFeatures:
            The `AvailableFeatures` services Object.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> available_features_service = power_bi_client.available_features()
        """

        return AvailableFeatures(session=self.power_bi_session)

    def capactities(self) -> Capacities:
        """Used to access the `Capacities` Services and metadata.

        ### Returns
        ---
        Capacities:
            The `Capacities` services Object.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> capacities_service = power_bi_client.capactities()
        """

        return Capacities(session=self.power_bi_session)

    def pipelines(self) -> Pipelines:
        """Used to access the `Pipelines` Services and metadata.

        ### Returns
        ---
        Pipelines:
            The `Pipelines` services Object.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> pipelines_service = power_bi_client.pipelines()
        """

        return Pipelines(session=self.power_bi_session)

    def datasets(self) -> Datasets:
        """Used to access the `Datasets` Services and metadata.

        ### Returns
        ---
        Datasets:
            The `Datasets` services Object.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
            >>> datasets_service = power_bi_client.datasets()
        """

        return Datasets(session=self.power_bi_session)
