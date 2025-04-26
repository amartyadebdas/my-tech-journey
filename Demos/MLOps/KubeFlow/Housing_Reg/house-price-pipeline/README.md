# KubeFlow Implementation

This project shows a simple machine learning regression problem of house price prediction and
uses KubeFlow Pipeline to demonstrate it.

Here's a link to the documentation of this project:
https://docs.google.com/document/d/1nUOUh4pOrmCKhdv4w_IRECd7xWzRkx8UF_vkK2pYb0Y/edit?usp=sharing

Link to Kubeflow Documentation:
https://www.kubeflow.org/docs/

For KubeFlow setup:
https://github.com/kubeflow/manifests/tree/master

1. Install the dependencies: [Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download), [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), [Manifests](https://github.com/kubeflow/manifests?tab=readme-ov-file#installation), Kubeflow, <span title="sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"> Docker<span>.
2. Follow these steps:
    - `minikube start`
    - `kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80` (*I have used 8080:80*)

    This exposes the Kubeflow UI in the port [localhost:8080](http://localhost:8080/).

3. Run these files and get the `kubeflow_pipeline.yaml` file.
4. Host Kubeflow in any port you want to, I used [localhost:8080](http://localhost:8080/).
5. Upload the yaml file in the pipeline and run.

## 📌 Problem Statement
Build a machine learning pipeline that can predict house prices based on features like bedrooms, bathrooms, and square footage. The pipeline is constructed using Kubeflow Pipelines and runs inside a local Kubernetes cluster provided by Minikube.

## ✅ ML Pipeline Approach
The pipeline consists of four main stages:

 >**Data Generation:**
    Generate synthetic housing data using NumPy and pandas.

 >**Data Processing:**
    Split the data into training and testing sets using Scikit-learn.

 >**Model Training:**
    Train a Linear Regression model to predict house prices.

 >**Model Evaluation:**
    Evaluate the model's performance using Mean Squared Error (MSE).

Each stage is implemented as a Kubeflow component using @dsl.component.

## 🚀 Setup Instructions
### Prerequisites
1. **Python 3.9+**

2. **Docker**

3. **Minikube**

4. **kubectl**

5. **KFP SDK**

# Steps:
## 1. 📂 Clone the Repository
```bash
git clone -b kubeflow_mlflow https://git.impressicocrm.com/mlops/dev_mlops.git
```

## 2. Navigate to the directory
```cd dev_mlops/KubeFlow/Housing_Reg/house-price-pipeline/```

## 3. Install minikube:
```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```
## 4. Install kubectl:
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

## 5. Install kfp
```bash
pip install kfp
```

## 6. 🚀 Start Minikube
```minikube start --driver=docker```

## 7. 🔌 Port Forward Kubeflow Dashboard
    kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
Access Kubeflow at: [http://localhost:8080](http://localhost:8080)

## 8. 🏗️ Compile and Upload the Pipeline
    python pipeline.py
> This generates `kubeflow_pipeline.yaml`.

Upload it in the Kubeflow Pipelines UI and run the pipeline.

## 🎯 Why Kubeflow?
**Kubeflow Pipelines help**:

1. Track and manage experiments

2. Reuse pipeline components

3. Scale pipelines easily with Kubernetes

4. Visually monitor workflow execution

**When to Use**:
1. When you're building modular ML pipelines

2. For experiment tracking, reproducibility, and scalable training

## ❌ When Not to Use Kubeflow
1. For very lightweight ML tasks or early-stage experimentation

2. When you're not using Kubernetes

3. If your team lacks Kubernetes expertise

## 📈 Evaluation Metric
We used **Mean Squared Error (MSE)** to evaluate model performance.
For example:

> MSE = 2 means the average squared prediction error is 2 units.


> R² = 0.87 means the model explains 87% of the variability in the target variable.
> Values closer to 1 indicate a stronger fit between predictions and actual outcomes.

## 📬 Contact
For queries or suggestions, feel free to reach out!
Email: [amartyadebdas@gmail.com](amartyadebdas@gmail.com)

## 🙌 Credits
This project was created by **Amartya Debdas**.
