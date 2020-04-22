# Installation

Les librairies suivantes sont nécessaires pour cette formation :
* Python 3.6+
* numpy
* [matplotlib](https://matplotlib.org/users/installing.html)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
* [Jupyter notebook](https://jupyter.readthedocs.io/en/latest/install.html)
* [ML Flow](https://www.mlflow.org/docs/latest/quickstart.html)
* [scikit-learn](https://scikit-learn.org/stable/install.html)

Nous allons voir comment les installer.


## Les étapes d'installation
1. **Si vous n'avez pas déjà Python installé sur votre machine**, installez Anaconda en téléchargeant la version correspondant à votre OS et en suivant les instructions disponibles [ici](https://docs.anaconda.com/anaconda/install/).


2. Téléchargez ou clonez le répertoire git disponible [ici](https://github.com/meteofrance/formation-mlflow).


3. (*Optionnel*) Si vous utilisez Python régulièrement, afin de préserver votre environnement et configuration de travail, vous pouvez **créer un environnement virtuel Python**. Ainsi les modifications faites lors de l'installation seront faites uniquement dans ce nouvel environnement. Voici la marche à suivre avec **Conda** :
    1. Pour créer un nouvel environnement : ouvrez un terminal et entrez ```conda create -n my_new_env_name python=3.7```
    2. Pour activer le nouvel environnement : ```conda activate my_new_env_name```
    3. Pour revenir à votre configuration habituelle quand vous avez fini de travailler sur la formation MLFLow : ```conda deactivate```

4. Dans un terminal, naviguez jusqu'au dossier de la formation. Installez les librairies avec la commande suivante : ```pip install -r requirements.txt```.

## Vérification de l'installation

Ouvrez un terminal et naviguez jusqu'au dossier de la formation. Entrez ```jupyter notebook```. L'interface Jupyter doit s'ouvrir dans votre navigateur. Cliquez sur le notebook ```formation-mlflow.ipynb```. Le notebook doit s'ouvrir dans un nouvel onglet. Exécutez la première cellule qui contient les instructions ```import```. Aucun message d'erreur ne doit apparaître.

Si vous avez des messages d'erreur du type ```Import error : Could not import ...``` , revenez à l'étape 4. Si vous avez toujours des messages d'erreur ensuite, contactez [lea.berthomier@meteo.fr](lea.berthomier@meteo.fr).

