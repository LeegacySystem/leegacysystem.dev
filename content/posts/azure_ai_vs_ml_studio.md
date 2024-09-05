---
title: 'Azure AI vs ML Studio'
date: 2024-09-04T20:50:26+01:00
tags: 
- Azure 
- AI
- ML
- GenAI
- OpenAi
- Terraform
---

I probably first used the Azure Machine Learning service mid-2022, just before OpenAI's ChatGPT exploded in popularity.

This was before Azure OpenAI service and its corresponding Azure OpenAI studio was available, even back then I noticed the Machine Learning workspace studio UI was changing reguarly with new features being added. After Azure OpenAI was released, the pace of change seemed to accelerate even more.

I’ll admit, I didn’t document any of these UI changes, and I’m definitely not motivated enough to sift through release logs so I’m relying on my sub-par memory here, but I swear the ML studio UI was different!

Microsoft has since introduced AI Studio, which I haven’t followed as closely. From my initial reading, it seems to be the recommended replacement for Azure OpenAI Studio, with added features for centralized governance.

AI Studio can be deployed as a Hub for central governance or as a Project, which must link back to a Hub. Interestingly, both AI Studio Hub and AI Studio Project are just Machine Learning workspaces under the hood.

You can see this in the resource providers for both being "Microsoft.MachineLearningServices/workspaces" with the difference being the value of the kind attribute. Basically Kind:hub is a hub, Kind:project is a project and lastly Kind:Default is an ML Workspace. If you jump to the bottom of this post you'll find some terraform code snippets I've pulled from my personal dev tenant.

I was already struggling to keep up with this studio naming game!

<div style="text-align: center;">
    <img src="/images/posts/2024/09/04/ml_ai_studio_post.png" alt="spider-man meme" />
</div>

At least on the surface it does still look like the Machine Learning Workspaces should be used for development of internal ML models on internal data, whereas AI studio is targeting GenAI/AI app development.

I would bet money that the Azure Machine Learning service might be due for a rebranding or slow merger with AI studio. If my prediction doesn't come true and you're a future person that bet against me, feel free to collect your reward [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

If the weather takes a turn for the worse this weekend I might do a follow-up post focusing more on AI Studio for my own understanding.

## Code Samples 

**Machine Learning Workspace Creation**
kind = "Default" will give a traditional Machine Learning Workspace and accompanying ML Studio.

```go
resource "azapi_resource" "mlworkspace" {
  type      = "Microsoft.MachineLearningServices/workspaces@2024-04-01"
  name      = "mlworkspace"
  location  = "uksouth"
  parent_id = azurerm_resource_group.mlworkspace.id

  identity {
    type = "SystemAssigned"
  }

  body = jsonencode({
    properties = {
      description    = "mlworkspace test"
      friendlyName   = "mlworkspace test"
      hubResourceId = azapi_resource.hub.id

      storageAccount = azurerm_storage_account.hub.id
      keyVault       = azurerm_key_vault.hub.id
      applicationInsights = azurerm_application_insights.hub.id

    }

    sku = {
      name = "Basic",
      tier = "Basic"
    }

    kind = "Default"
  })
}
```

**AI Studio Hub**
Kind = "Hub" will give an AI Hub resource. 

```go
resource "azapi_resource" "hub" {
  type      = "Microsoft.MachineLearningServices/workspaces@2024-04-01-preview"
  name      = "hub"
  location  = "uksouth"
  parent_id = azurerm_resource_group.hub.id

  identity {
    type = "SystemAssigned"
  }

  body = jsonencode({
    properties = {
      description    = "hub test"
      friendlyName   = "hub test"
      storageAccount = azurerm_storage_account.hub.id
      keyVault       = azurerm_key_vault.hub.id

      applicationInsights = azurerm_application_insights.hub.id
    }
    kind = "Hub"
  })
}
```

**AI Studio Project**
King = "project" will give you an AI Project. 

The important point here is that "hubResourceId" is a required arguement while storageAccount, keyVault, applicationInsights are not. This is because the project inherits the configuration from the hub.

```go
resource "azapi_resource" "project" {
  type      = "Microsoft.MachineLearningServices/workspaces@2024-04-01-preview"
  name      = "project"
  location  = "uksouth"
  parent_id = azurerm_resource_group.project.id

  identity {
    type = "SystemAssigned"
  }

  body = jsonencode({
    properties = {
      description    = "project test"
      friendlyName   = "project test"
      hubResourceId = azapi_resource.hub.id
    }
    kind = "project"
  })
}

```
