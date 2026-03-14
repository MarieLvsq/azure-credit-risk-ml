import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

load_dotenv()

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")
workspace_name = os.getenv("AZURE_ML_WORKSPACE")

credential = DefaultAzureCredential()

ml_client = MLClient(
    credential=credential,
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace_name,
)

workspace = ml_client.workspaces.get(workspace_name)
print(f"Connected to workspace: {workspace.name}")
print(f"Location: {workspace.location}")