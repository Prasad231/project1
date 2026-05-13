
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "project1green231"
    container_name       = "tfstate-container"
    key                  = "aks.tfstate"
  }
}

