from src.animalDetection import logger
from animalDetection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from animalDetection.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from animalDetection.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx================================x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare Base Model'

try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx================================x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Training'

try:
    logger.info(f'>>>>>>> Stage {STAGE_NAME} started <<<<<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx================================x')
except Exception as e:
    logger.exception(e)
    raise e