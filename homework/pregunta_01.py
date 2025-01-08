# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os
import pandas as pd
import csv

def save_output(dataframe, name, output_directory="files/output"):
    """Save output to a file."""

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    dataframe.to_csv(
        f"{output_directory}/{name}.csv",
        index=False,
    )

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    # Leer archivos y crear dataset TRAIN
    train_dataset = []
    # make a for loop to read the train/test directories
    for root, directories, _ in os.walk("files/input/train"):
        # make a for loop to read the sentiment directories
        for dir in directories:
            # get the sentiment of the directory
            sentiment = dir
            # get the path of the directory
            dir_path = os.path.join(root, dir)
            # make a for loop to read the phrases in the file
            for file in os.listdir(os.path.join(root, dir)):
                # get the path of the file
                path_to_file= os.path.join(dir_path, file)
                # open the file and read the phrase
                with open(path_to_file, "r") as f:
                    phrase = f.read()
                    train_dataset.append([phrase, sentiment])

    # Leer archivos y crear dataset TEST
    test_dataset = []
    # make a for loop to read the train/test directories
    for root, directories, _ in os.walk("files/input/test"):
        # make a for loop to read the sentiment directories
        for dir in directories:
            # get the sentiment of the directory
            sentiment = dir
            # get the path of the directory
            dir_path = os.path.join(root, dir)
            # make a for loop to read the phrases in the file
            for file in os.listdir(os.path.join(root, dir)):
                # get the path of the file
                path_to_file= os.path.join(dir_path, file)
                # open the file and read the phrase
                with open(path_to_file, "r") as f:
                    phrase = f.read()
                    test_dataset.append([phrase, sentiment])

    # Guardar dataset
    train_df = pd.DataFrame(train_dataset)
    test_df = pd.DataFrame(test_dataset)
    
    train_df.columns = ["phrase", "target"]
    test_df.columns = ["phrase", "target"]

    save_output(train_df, "train_dataset")
    save_output(test_df, "test_dataset")

pregunta_01()