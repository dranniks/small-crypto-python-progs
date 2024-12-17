use std::collections::HashSet;
use std::hash::Hash;

pub struct Unique<I> {
    iter: I,
    seen: HashSet<String>,
    ignore_case: bool,
}

impl<I, T> Unique<I>
where
    I: Iterator<Item = T>,
    T: Hash + Eq + ToString,
{
    pub fn new(iter: I, ignore_case: bool) -> Self {
        Unique {
            iter,
            seen: HashSet::new(),
            ignore_case,
        }
    }
}

impl<I, T> Iterator for Unique<I>
where
    I: Iterator<Item = T>,
    T: Hash + Eq + ToString,
{
    type Item = T;

    fn next(&mut self) -> Option<Self::Item> {
        while let Some(item) = self.iter.next() {
            // Преобразуем элемент в строку, учитывая регистр
            let key = if self.ignore_case {
                item.to_string().to_lowercase()
            } else {
                item.to_string()
            };

            // Проверяем, встречался ли элемент ранее
            if !self.seen.contains(&key) {
                self.seen.insert(key);
                return Some(item); // Возвращаем уникальный элемент
            }
        }
        None // Если элементов больше нет, возвращаем None
    }
}

// Пример использования
fn main() {
    let data = vec!["a".to_string(), "A".to_string(), "b".to_string(), "B".to_string(), "a".to_string()];
    
    let unique_iter = Unique::new(data.into_iter(), false);
    for value in unique_iter {
        println!("{}", value); // Выводит: a A b B a
    }

    let data_case_insensitive = vec!["a".to_string(), "A".to_string(), "b".to_string(), "B".to_string()];
    
    let unique_iter_case_insensitive = Unique::new(data_case_insensitive.into_iter(), true);
    for value in unique_iter_case_insensitive {
        println!("{}", value); // Выводит: a b
    }

    // Пример с числами
    let numbers = vec![1, 2, 2, 3, 1];
    
    let unique_numbers_iter = Unique::new(numbers.into_iter(), false);
    for value in unique_numbers_iter {
        println!("{}", value); // Выводит: 1 2 3
    }
}
