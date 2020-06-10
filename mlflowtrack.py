
import mlflow

class mlflowTracking:
    
    def __init__(self,url,experiment_name,run_name):
        mlflow.set_tracking_uri(url)
        mlflow.set_experiment(experiment_name)
        mlflow_id=mlflow.get_experiment_by_name(experiment_name)
        with mlflow.start_run(run_name= run_name ,experiment_id=mlflow_id.experiment_id):
            self.run_id=mlflow.get_artifact_uri().split('/')[-2] #get run_id
        mlflow.end_run()
    
    def log_param(self, params):
        with mlflow.start_run(run_id= self.run_id):
            mlflow.log_params(params)
        mlflow.end_run()

    def log_metrics(self,set_metrics):
        with mlflow.start_run(run_id=self.run_id):
            step=set_metrics.pop("step")
            mlflow.log_metrics(set_metrics,step=step)
        mlflow.end_run()

    def log_tag(self, tag):
        with mlflow.start_run(run_id= self.run_id):
            mlflow.set_tags(set_tag)
        mlflow.end_run()
    
    def log_artifact(self,filename,data):
        with mlflow.start_run(run_id=self.run_id):
            with open(filename, "a+") as f:
                f.write(f"{data}")
                mlflow.log_artifact(filename)
        mlflow.end_run()


# URL="http://127.0.0.1:5000"
# EXPERIMENT_NAME="paritoshy"
# RUN_NAME = "TPS 1.0" # (model name + model version) 

# PARAMS= {
#     "Model Version":"",
#     "Platform":"",   # (tensorflow, pytorch, tensorflow rt)
#     "Platform Version":"",
#     "Backbone":"TPS,ATTENTION", #(if any)
    
#     "Training Set":80,
#     "Validation Set":10,
#     "Test Set":10,
    
#     "Learning Rate":"",
#     "Optimizer":"",
#     "Total Epoch":"",
#     "Batch":"",
    
#     "Training Time":"",
#     "Training Stop Epoch":"",
# }

# SET_METRICS={
#     "itration":300,
#     "loss":6,
#     "validation loss":1
# }

# runid=create(URL,EXPERIMENT_NAME,RUN_NAME,PARAMS,SET_TAG)
# log_metrics(runid,SET_METRICS)
# log_artifact(runid,"out.txt","hello world")
# log_params(runid,{"precsion":90,"recall":49})