# my-tf-explain

Оригинальный проект : https://github.com/sicara/tf-explain

Склонируйте репозиторий

`git clone https://github.com/RodionovDenis/my-tf-explain.git`

Перейдите в склонированную папку "my-tf-explain"

`cd my-tf-explain`

Далее необходимо сбилдить докер по текущему Dockerfile

`docker build . --tag explainer`

Запускаем докер explainer со свойством монтирования в папку my-tf-explain/images/actual

`docker run -v $(pwd)/images/actual:/src explainer`

Если поле работы докера не удается удалить папку actual, воспользуйтесь командой, которая изменяет владельщика папки actual

`sudo chown -R $(whoami):$(whoami) actual`
