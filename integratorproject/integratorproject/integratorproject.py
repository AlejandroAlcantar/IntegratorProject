import joblib
from Load.load_data import DataRetriever
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from Train.train_data import WaterQualityDataPipeline

DATASETS_DIR = 'integratorproject\\integratorproject\\Data\\water_potability.csv'
DROP_COLS = []


SEED_SPLIT = 404

TARGET = 'Potability'

FEATURES = [
    'ph',
    'Hardness',
    'Solids',
    'Chloramines',
    'Sulfate',
    'Conductivity',
    'Organic_carbon',
    'Trihalomethanes',
    'Turbidity',
    'Potability']

NUMERICAL_VARS = [
    'ph',
    'Hardness',
    'Solids',
    'Chloramines',
    'Sulfate',
    'Conductivity',
    'Organic_carbon',
    'Trihalomethanes',
    'Turbidity',
    'Potability']

CATEGORICAL_VARS = []


NUMERICAL_VARS_WITH_NA = [
    'ph',
    'Hardness',
    'Solids',
    'Chloramines',
    'Sulfate',
    'Conductivity',
    'Organic_carbon',
    'Trihalomethanes',
    'Turbidity']

CATEGORICAL_VARS_WITH_NA = []

SEED_MODEL = 404

SELECTED_FEATURES = [
    'ph',
    'Hardness',
    'Solids',
    'Chloramines',
    'Sulfate',
    'Conductivity',
    'Organic_carbon',
    'Trihalomethanes',
    'Turbidity']

TRAINED_MODEL_DIR = './integratorproject/integratorproject/Models/'
PIPELINE_NAME = 'logistic_regression'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output.pkl'

if __name__ == "__main__":

    #    print(os.getcwd())

    # Retrieve data
    data_retriever = DataRetriever(DATASETS_DIR)
    result = data_retriever.retrieve_data()
    print(result)

    # Instantiate the TitanicDataPipeline class
    waterquality_data_pipeline = WaterQualityDataPipeline(
        seed_model=SEED_MODEL,
        numerical_vars_with_na=NUMERICAL_VARS_WITH_NA,
        selected_features=SELECTED_FEATURES)
    waterquality_data_pipeline.create_pipeline()

    # # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        result.drop(TARGET, axis=1),
        result[TARGET],
        test_size=0.2,
        random_state=404
    )

    X_transformed = waterquality_data_pipeline.PIPELINE.fit_transform(X_train)
    logistic_regression_model = waterquality_data_pipeline.fit_logistic_regression(
        X_transformed, y_train)

    X_test_transformed = waterquality_data_pipeline.PIPELINE.fit_transform(
        X_test)
    class_pred = logistic_regression_model.predict(X_test_transformed)
    proba_pred = logistic_regression_model.predict_proba(X_test_transformed)[
        :, 1]

    print(class_pred)

    print(f'test roc-auc : {roc_auc_score(y_test, proba_pred)}')
    print(f'test accuracy: {accuracy_score(y_test, class_pred)}')

    # # # Save the model using joblib
    save_path = TRAINED_MODEL_DIR + PIPELINE_SAVE_FILE
    joblib.dump(logistic_regression_model, save_path)
    print(f"Model saved in {save_path}")
