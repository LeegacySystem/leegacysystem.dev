






Questions/things to check:
___
* Does AI Studio have autoMl?


Experimenting:
___
* AI studio hub RBAC do not inherit down to project, would need to be done at a higher level


Doc review:
__
* Build generative AI applications
* Works with VS  Code desktop & web?
* High and low-code
* build, test, and deploy ML models
* AI hub provides collaborative environment with shared 
* AI project allows to save state?
* AI studio has no cost, but the services created and consumed via it do so potential to get complicated

Integrations with, AI Services, OpenAI Service, Model Catalog managed compute & serverless, model benchmarks

Hubs: 
* Common security and network configration spanning projects.
* Compue for interactive development, fine-tuning, open source and severless model deployments
* Integrations with other AI services (AOAI, Search), shared between projects
* Child projects
* Single storage account for data upload & artifact storage.

Project:
* Dev tools for building and customising AI apps.
* Shared components from paren hub (compute instaces, network etc)
* Isolated container within parent hub storage account

Hubs centrally manage projects, as many projects as needed can be created.
Projects can be used as organise work, data boundaries and or restrict access
Connections are used to integrate AI studio with other services like AI search, sounds similar to ADO service connections. 
These connections can be shared across projects.
Connections can use key-based access (assumed bad) or Entra ID passthrough sounds like delegated to me.

Generally it makes sense to allign hubs to departments where data requirements are similar. For example if you might a customer services AI hub and a innovation hub, ML Ops might dictate dev,test & prod so that would be 6 hubs total for full isolation.

hub depeonds on - https://learn.microsoft.com/en-us/azure/ai-studio/concepts/architecture#azure-resource-types-and-providers

Microsoft managed resources - Managed compute, Managed VNET, Metadata storage
Managed compute requires vulnerability management? https://learn.microsoft.com/en-us/azure/ai-studio/concepts/vulnerability-management

RBAC & Control Plane Proxy:
* none hub services RBAC is seperate from hub
* AI studio offers control plane proxy where operations are AI studio services makes calls to other resources (AOAI), how does this work with user perms?

Each project has:
* Service principal with blob data contrib on the stroage account
* unique id (workspace id)
* Containers in storage account, prefixed with workspace id
* Role assignment has ABAC condition to limit SP access to containers with matching prefix, so no cross project container access

Hub storage account containers:
* {workspace-ID}-azureml    - metrics, models, components
* {workspace-ID}-blobstore  - uploaded data, code snapshots, pipeline data cache
* {workspace-ID}-code       - Notebooks, comput instance, prompt flow
* {workspace-ID}-file       - alternate data upload folder

* AI content safety works for Azure OpenAi and open source models
* Cost aren't tracked well within hubs or projects, so hubs and project should be kept to their own resource groups/subscriptions
* Prompt flow within custom environments require Azure Container Registry

RBAC: 
* When a user does not have a permission to perform an action, generally the studio will not show that option.
* Only owner or contributor can create hubs
* There is not currently a custom role to create hubs
* Built-in role like Azure AI Developer include permissions across services (ML & Cognitive)
* AI Studio (hub view) has a user management section, not sure how this plays with Azure RBAC

Comput Vuln Mgmt:
* Microsoft manages host OS virtual machine (VM) images for compute instances and serverless compute clusters
* Monthly update frequency
* Canonical Ubuntu images
* Microsoft updates system packages when updates are available.
* Microsoft checks and validates any machine learning packages that might require an upgrade. 
* All VM images are built on secure subscriptions that run vulnerability scanning regularly. 
* Microsoft applies hotfixes if vulnerabilities surface. Microsoft rolls out hotfixes within 72 hours for serverless compute clusters and within a week for compute instances.

* Base docker images - Microsoft releases updates for supported images every two weeks to address vulnerabilities. 
* Using the :latest tag or pinning to a particular image version might be a tradeoff between security and environment reproducibility for your machine learning job.
* AI Studio doesn't delete images from Azure Container Registry but defender for container registry could be used.

* Compute Instances, Microsoft doesn't actively scan compute nodes for vulnerabilities while they're in use.


Interopability:
https://learn.microsoft.com/en-us/azure/machine-learning/concept-hub-workspace?view=azureml-api-2


#-----------------------------------------






* Write about using Machine Learning Workspace since Summer 2022.
* Comment that it was before the OpenAI ChatGPT exploding in popularity

* Comment on the fact that ML workspace stuido constantly changed and really picked up after Chatgpt.
* Comment on Open Ai Studio changing at a similar pace.


* Not following AI studio as closely

* AI Studio now seems to be recommended over Open AI studio

* AI Studio Hub seems to be new and provides centralisation/governance over machine learning workpsaces

* In the background AI Studio is just a machine learning workspace, see "Microsoft.MachineLearningServices/workspaces" https://learn.microsoft.com/en-us/azure/ai-studio/concepts/architecture

* I suspect Azure machine learning workspaces are going to be rebranded.
* compute nodes use the latest OS version is a shared responsibility.
* Nodes that aren't idle can't be updated to the latest VM image.
* Endpoints automatically receive OS host image updates that include vulnerability fixes

After you deploy a compute instance, it isn't actively updated:
    * Re-create a compute instance to get the latest OS image (recommended).
    * Regularly update OS and Python packages.

Disaster Recovery:
resources MS responsible for:
    AI Studio Infra
    Compute Instance

Resources I am responsible for:
    Azure Storage
    Key Vault
    Container Registry
    App Insights
    Any connections


