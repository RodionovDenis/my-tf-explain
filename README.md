# my-tf-explain

Original project : https://github.com/sicara/tf-explain

`git clone https://github.com/RodionovDenis/my-tf-explain.git`

`cd my-tf-explain`

`docker build . --tag explainer`

`docker run -v $(pwd)/images/actual:/src explainer`

`sudo chown -R $(whoami):$(whoami) actual`
