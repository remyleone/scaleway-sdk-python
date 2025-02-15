# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    random_name,
    validate_path_param,
    fetch_all_pages,
)
from .types import (
    ListProjectsRequestOrderBy,
    ListProjectsResponse,
    Project,
    ProjectApiCreateProjectRequest,
    ProjectApiUpdateProjectRequest,
)
from .marshalling import (
    unmarshal_Project,
    unmarshal_ListProjectsResponse,
    marshal_ProjectApiCreateProjectRequest,
    marshal_ProjectApiUpdateProjectRequest,
)


class AccountV3ProjectAPI(API):
    """
    This API allows you to manage projects.
    """

    def create_project(
        self,
        *,
        description: str,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
    ) -> Project:
        """
        Create a new Project for an Organization.
        Generate a new Project for an Organization, specifying its configuration including name and description.
        :param description: Description of the Project.
        :param name: Name of the Project.
        :param organization_id: Organization ID of the Project.
        :return: :class:`Project <Project>`

        Usage:
        ::

            result = api.create_project(
                description="example",
            )
        """

        res = self._request(
            "POST",
            "/account/v3/projects",
            body=marshal_ProjectApiCreateProjectRequest(
                ProjectApiCreateProjectRequest(
                    description=description,
                    name=name or random_name(prefix="proj"),
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())

    def list_projects(
        self,
        *,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProjectsRequestOrderBy] = None,
        project_ids: Optional[List[str]] = None,
    ) -> ListProjectsResponse:
        """
        List all Projects of an Organization.
        List all Projects of an Organization. The response will include the total number of Projects as well as their associated Organizations, names, and IDs. Other information includes the creation and update date of the Project.
        :param organization_id: Organization ID of the Project.
        :param name: Name of the Project.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned Projects.
        :param project_ids: Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
        :return: :class:`ListProjectsResponse <ListProjectsResponse>`

        Usage:
        ::

            result = api.list_projects()
        """

        res = self._request(
            "GET",
            "/account/v3/projects",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_ids": project_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListProjectsResponse(res.json())

    def list_projects_all(
        self,
        *,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListProjectsRequestOrderBy] = None,
        project_ids: Optional[List[str]] = None,
    ) -> List[Project]:
        """
        List all Projects of an Organization.
        List all Projects of an Organization. The response will include the total number of Projects as well as their associated Organizations, names, and IDs. Other information includes the creation and update date of the Project.
        :param organization_id: Organization ID of the Project.
        :param name: Name of the Project.
        :param page: Page number for the returned Projects.
        :param page_size: Maximum number of Project per page.
        :param order_by: Sort order of the returned Projects.
        :param project_ids: Project IDs to filter for. The results will be limited to any Projects with an ID in this array.
        :return: :class:`List[Project] <List[Project]>`

        Usage:
        ::

            result = api.list_projects_all()
        """

        return fetch_all_pages(
            type=ListProjectsResponse,
            key="projects",
            fetcher=self.list_projects,
            args={
                "organization_id": organization_id,
                "name": name,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_ids": project_ids,
            },
        )

    def get_project(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> Project:
        """
        Get an existing Project.
        Retrieve information about an existing Project, specified by its Project ID. Its full details, including ID, name and description, are returned in the response object.
        :param project_id: Project ID of the Project.
        :return: :class:`Project <Project>`

        Usage:
        ::

            result = api.get_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "GET",
            f"/account/v3/projects/{param_project_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())

    def delete_project(
        self,
        *,
        project_id: Optional[str] = None,
    ) -> None:
        """
        Delete an existing Project.
        Delete an existing Project, specified by its Project ID. The Project needs to be empty (meaning there are no resources left in it) to be deleted effectively. Note that deleting a Project is permanent, and cannot be undone.
        :param project_id: Project ID of the Project.

        Usage:
        ::

            result = api.delete_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "DELETE",
            f"/account/v3/projects/{param_project_id}",
        )

        self._throw_on_error(res)

    def update_project(
        self,
        *,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Project:
        """
        Update Project.
        Update the parameters of an existing Project, specified by its Project ID. These parameters include the name and description.
        :param project_id: Project ID of the Project.
        :param name: Name of the Project.
        :param description: Description of the Project.
        :return: :class:`Project <Project>`

        Usage:
        ::

            result = api.update_project()
        """

        param_project_id = validate_path_param(
            "project_id", project_id or self.client.default_project_id
        )

        res = self._request(
            "PATCH",
            f"/account/v3/projects/{param_project_id}",
            body=marshal_ProjectApiUpdateProjectRequest(
                ProjectApiUpdateProjectRequest(
                    project_id=project_id,
                    name=name,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Project(res.json())
