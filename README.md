# Applied Linear Algebra. Lab assignment 1.  
# Linear transformations.  
  
## 1. Що таке лінійні трансформації?  
**Лінійна трансформація** – це математичне перетворення, яке зберігає операції додавання і множення на скаляр. Для лінійності мають виконуватись:  
1. *Адитивність*: T(u+v)=T(u)+T(v)  
2. *Однорідність*: T(cu)=cT(u)  
  
## 2. Як і в яких галузях застосовуються лінійні трансформації?  
- *Комп'ютерна графіка*: Масштабування, обертання, відображення та трансляція об'єктів.  
- *Машинне навчання*: Зниження розмірності даних (наприклад, PCA), обробка даних у нейронних мережах.  
- *Економіка та фінанси*: Моделювання і аналіз даних.  
- *Інженерія*: Аналіз і моделювання систем, що описуються диференційними рівняннями.  
  
## 3. Що таке матриця лінійної трансформації та як її можна інтерпретувати?  
*Матриця лінійної трансформації* - матриця-представлення лінійних перетворень над векторами у векторному просторі. Тобто за допомогою матриці можна подати будь-яке лінійне відображення.  
  
Матрицю лінійної трансформації можна інтерпретувати як **набір дій над координатами вектора**. Кожна координата буде змінюватись під впливом трансформації і переходити в інші точки простору.  
  
## 4. Які особливості та властивості має матриця обертання?  
- Стовпці (і рядки) ортогональні один одному і мають одиничну довжину.
- Детермінант матриці обертання завжди дорівнює 1 або -1, але для власне обертання (без віддзеркалення) він дорівнює 1.
- Обертання не змінює довжини векторів і кути між ними.
  
## 5. Чи залежить фінальний результат від порядку трансформацій? Провести експерименти з фігурами або зображеннями з частин 1-2.  
Так, порядок лінійних трансформацій має значення. Якщо виконати дві різні трансформації по черзі, результат буде залежати від того, в якому порядку ці трансформації були виконані.  
Це теж саме, що з порядком множення матриць. В залежності від порядку проведених операцій з матрицями результат змінюється.  
  
Проведемо експеримент:  
1. Виконаємо віддзеркалення за віссю *y*, а потім обернемо довгоносу собачку на 45 градусів.  
![1](https://github.com/kseniiahanziuk/lab-1-applied-linear-algebra-khanziuk/assets/151023627/fe7a7247-7e59-414a-ae14-5e2ad3deca09)
2. Виконаємо обертання довгоносої собачки на 45 градусів, а потім віддзеркалення за віссю *y*.  
![2](https://github.com/kseniiahanziuk/lab-1-applied-linear-algebra-khanziuk/assets/151023627/3f5a8161-04fd-457e-b736-07c687c98bc4)  
Результати отримуємо різні. Це доводить, що порядок змін важливий.  

## 6. Була здійснена якась довільна лінійна трансформація; як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду? Чи завжди можна здійснити обернену трансформацію?  

Щоб знайти матрицю, яка поверне все до початкового вигляду (обернена матриця), потрібно знайти обернену матрицю до початкової матриці лінійної трансформації A.  
Обернена матриця A^−1 має властивість AA^−1=I. Знайти обернену матрицю можна за допомогою методу Гаусса, алгебраїчних перетворень чи методу LU-розкладу.  
  
Обернену матрицю можна знайти, якщо детермінант матриці A не дорівнює нулю. Якщо детермінант дорівнює нулю, матриця не має оберненої, і обернену трансформацію здійснити неможливо.  
  
## 7. Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)? А якщо більше 1? Дорівнює 1? Дорівнює 0?  
- Модуль визначника менше 1: трансформація стискає простір, зменшуючи об'єми фігур.  
- Модуль визначника більше 1: трансформація розтягує простір, збільшуючи об'єми фігур.  
- Модуль визначника дорівнює 1: трансформація зберігає об'єми, тобто це може бути обертання або відображення без зміни масштабу.  
- Визначник дорівнює 0: трансформація стискає простір до меншої розмірності, наприклад, переводячи 3D-простір у площину або лінію.  
  
  
## Висновки, які елементи лінійної трансформації на що впливають:  
- Елементи матриці **масштабування** стискають чи розтягують матрицю по осях в залежності від коефіцієнту.  
- Елементи матриці **обертання** утворюють ортогональну матрйцю та визначають орієнтацію та кут обертання фігури.  
- Елементи матриці **відображення** за рахунок зміни знаків на певному векторі визначають напрямок фігури відповідно до осі обертання.  