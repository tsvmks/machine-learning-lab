# machine-learning-lab

## Git 
>https://learngitbranching.js.org/?locale=ru_RU
>https://git-scm.com/book/ru/v2

-------------------------------------------------------
## КНИГИ

Алгоритмы
Простыми словами и достаточно информативно
"Грокаем алгоритмы" Адитья Бхаргава (есть pdf)

Статистика
> "Статистика и котики" Владимир Савельев (есть pdf)

Машинное обучение
> "Машинное обучение" Бринк Хенрик, Ричардс Джозеф, Феверолф Марк (есть pdf)

Анализ временных рядов
> "Практический анализ временных рядов" Эйлин Нильсен (есть pdf)

-------------------------------------------------------
## ПРАКТИЧЕСКИЕ НАВЫКИ

Языки и билиотеки
> Python. Нужно знать базовый синтаксис, уметь работать с различными типами файлов (CSV, Excel, JSON, XML), 
> уметь подключаться к базе данных и импортировать данные себе в среду, владеть библиотеками Pandas и Numpy, 
> владеть библиотеками для визуализации данных (Matplotlib, Plotly, Seaborn)
> 
> R. уметь работать с различными типами файлов (CSV, Excel, JSON, XML), владеть библиотеками data.table.

--------------------------------------------------------

## МАШИННОЕ ОБУЧЕНИЕ

- Классическое обучение
	- С учителем
		- Регрессия (Цикл статей https://medium.com/machine-learning-for-humans/why-machine-learning-matters-6164faf1df12)
			Linear Regression (http://www.machinelearning.ru/wiki/index.php?title=%D0%9B%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D0%B0%D1%8F_%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F_%28%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%29)
			Polynomial Regression
		- Классификация
			K-NN (https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_k-%D0%B1%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B8%D1%85_%D1%81%D0%BE%D1%81%D0%B5%D0%B4%D0%B5%D0%B9)
			Naive Bayes (https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_%D0%B1%D0%B0%D0%B9%D0%B5%D1%81%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80) 
			SVM (https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%BE%D0%BF%D0%BE%D1%80%D0%BD%D1%8B%D1%85_%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2)
			Decision Trees (https://logic.pdmi.ras.ru/~sergey/teaching/mlcsclub/02-dectrees.pdf)
			Logistical Regression (https://ru.wikipedia.org/wiki/%D0%9B%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F)
	- Без учителя
		- Кластеризация (https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68	)
			K-Means (https://en.wikipedia.org/wiki/K-means_clustering)
			Mean shift (https://en.wikipedia.org/wiki/Mean_shift)
			DBScan (https://en.wikipedia.org/wiki/DBSCAN)
		- Поиск правил (ассоциация) (https://en.wikipedia.org/wiki/Association_rule_learning)			
		- Обобщение (https://habr.com/ru/post/275273/, https://habr.com/ru/company/yandex/blog/241455/)
			PCA (https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D1%85_%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82)
			LSA (https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%80%D0%BE%D1%8F%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%BD%D1%8B%D0%B9_%D0%BB%D0%B0%D1%82%D0%B5%D0%BD%D1%82%D0%BD%D0%BE-%D1%81%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7)
- Ансамблевые методы (поисковые агоритмы)
	Стекинг
	Беггинг	(https://en.wikipedia.org/wiki/Bootstrap_aggregating)
		Random Forest (https://ru.wikipedia.org/wiki/Random_forest)
	Бустинг (https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db)
		XGBoost
- Обучение с подкреплением
	Q-обучение(роботы-пылесосы, игры) (https://ru.wikipedia.org/wiki/Q-%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5)
- Нейросети и глубокое обучение
	CNN
	RNN

## ОЦЕНКА И ОПТИМИЗАЦИЯ МОДЕЛЕЙ
	MSE, RMSE


## АНАЛИЗ ВРЕМЕННЫХ РЯДОВ 
- Выявление рядов
- Методы исследования
- Статистические модели для временных рядов(AR, MA, ARIMA, VAR)
- Машинное обучение для анализа временных рядов
- Оценка ошибок


