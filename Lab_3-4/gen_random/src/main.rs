use rand::Rng;

fn gen_random(count: usize, min: i32, max: i32) -> Vec<i32> {
    let mut rng = rand::thread_rng(); // Создаем генератор случайных чисел
    let mut numbers = Vec::new(); // Создаем пустой вектор для хранения чисел

    for _ in 0..count { // Цикл для генерации count случайных чисел
        let number = rng.gen_range(min..=max); // Генерируем случайное число в диапазоне
        numbers.push(number); // Добавляем его в вектор
    }

    numbers // Возвращаем вектор с сгенерированными числами
}

fn main() {
    let count = 5; // Количество случайных чисел
    let min = 1; // Минимальное значение
    let max = 3; // Максимальное значение

    let random_numbers = gen_random(count, min, max); // Генерируем случайные числа
    println!("{:?}", random_numbers); // Выводим результат
}