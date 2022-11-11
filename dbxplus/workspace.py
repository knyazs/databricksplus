def getWorkspaceId(spark):
    return spark.conf.get("spark.databricks.workspaceUrl").split('.')[0];