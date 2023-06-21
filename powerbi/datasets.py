from typing import Dict
from powerbi.session import PowerBiSession


class Datasets():

    def __init__(self, session: PowerBiSession):
        """Initializes the `Datasets` object.

        ### Parameters
        ----
        session : object
            An authenticated session for our Microsoft PowerBi Client.

        ### Usage
        ----
            >>> reports_service = power_bi_client.reports()
        """

        # Set the session.
        self.power_bi_session= session

        # Set the endpoint.
        self.endpoint = 'myorg/datasets'

    def get_datasets(self) -> Dict:
        """Returns a list of reports from "My Workspace".

        ### Returns
        ----
        Dict
            A collection of `Dataset` objects.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.get_datasets()
        """
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=self.endpoint
        )

        return content

    def get_dataset(self, dataset_id: str) -> Dict:
        """Returns a specific dataset from "My Workspace".

        ### Parameters
        ----
        dataset_id : str
            The dataset ID.

        ### Returns
        ----
        Dict
            A `Dataset` object.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.get_dataset(dataset_id='dataset_id')
        """
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'{self.endpoint}/{dataset_id}'
        )

        return content

    def get_dataset_in_group(self, group_id: str, dataset_id: str) -> Dict:
        """Returns a specific dataset from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        dataset_id : str
            The dataset ID.

        ### Returns
        ----
        Dict
            A `Dataset` object.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.get_dataset_in_group(
                    group_id='group_id',
                    dataset_id='dataset_id'
                )
        """
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/datasets/{dataset_id}'
        )

        return content

    def get_datasets_in_group(self, group_id: str) -> Dict:
        """Returns a list of datasets from the specified workspace.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        ### Returns
        ----
        Dict
            A collection of `Dataset` objects.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.get_datasets_in_group(group_id='group_id')
        """
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/datasets'
        )

        return content

    def refresh_dataset(self, dataset: str) -> int:
        """Refreshes the specified dataset.

        ### Parameters
        ----
        dataset : str
            The dataset ID.

        ### Returns
        ----
        int
            The HTTP response code.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.refresh_dataset(dataset='dataset_id')
        """
        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'{self.endpoint}/{dataset}/refreshes'
        )

        return content

    def refresh_dataset_in_group(self, group_id: str, dataset: str) -> int:
        """Refreshes the specified dataset.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        dataset : str
            The dataset ID.

        ### Returns
        ----
        int
            The HTTP response code.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.refresh_dataset_in_group(
                    group_id='group_id',
                    dataset='dataset_id'
                )
        """
        content = self.power_bi_session.make_request(
            method='post',
            endpoint=f'myorg/groups/{group_id}/datasets/{dataset}/refreshes'
        )

        return content

    def get_refresh_history(self, dataset: str, stop = 500) -> Dict:
        """Returns the refresh history of the specified dataset.

        ### Parameters
        ----
        dataset : str
            The dataset ID.

        ### Returns
        ----
        Dict
            A collection of `Refresh` objects.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.get_refresh_history(dataset='dataset_id')
        """
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'{self.endpoint}/{dataset}/refreshes?$top={stop}'
        )

        return content

    def get_refresh_history_in_group(self, group_id: str, dataset: str, stop = 500) -> Dict:
        """Returns the refresh history of the specified dataset.

        ### Parameters
        ----
        group_id : str
            The workspace ID.

        dataset : str
            The dataset ID.

        ### Returns
        ----
        Dict
            A collection of `Refresh` objects.

        ### Usage
        ----
            >>> reports_service = power_bi_client.datasets()
            >>> reports_service.get_refresh_history_in_group(
                    group_id='group_id',
                    dataset='dataset_id'
                )
        """
        content = self.power_bi_session.make_request(
            method='get',
            endpoint=f'myorg/groups/{group_id}/datasets/{dataset}/refreshes?$top={stop}'
        )

        return content
