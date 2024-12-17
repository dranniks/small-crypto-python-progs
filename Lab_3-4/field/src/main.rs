use std::collections::HashMap;

fn field<'a>(
    goods: &'a [HashMap<String, Option<String>>],
    keys: &'a [&'a str],
) -> impl Iterator<Item = HashMap<String, String>> + 'a {
    goods.iter().map(move |item| {
        let mut result = HashMap::new();
        
        for &key in keys {
            if let Some(value) = item.get(key).and_then(|v| v.as_ref()) {
                result.insert(key.to_string(), value.clone());
            }
        }

        result
    })
}

fn main() {
    let goods = vec![
        HashMap::from([
            ("title".to_string(), Some("Ковер".to_string())),
            ("price".to_string(), Some("2000".to_string())),
            ("color".to_string(), Some("green".to_string())),
        ]),
        HashMap::from([
            ("title".to_string(), Some("Диван для отдыха".to_string())),
            ("price".to_string(), Some("5000".to_string())),
            ("color".to_string(), None),
        ]),
    ];

    let titles: Vec<_> = field(&goods, &["title"]).filter_map(|x| x.get("title").cloned()).collect();
    println!("{:?}", titles);
    
    let items: Vec<_> = field(&goods, &["title", "price", "color"]).collect();
    
    // Преобразуем HashMap в вектор пар для сохранения порядка
    let ordered_items: Vec<_> = items.iter().map(|item| {
        let mut ordered: Vec<(String, String)> = Vec::new();
        for &key in ["title", "price", "color"].iter() {
            if let Some(value) = item.get(key) {
                ordered.push((key.to_string(), value.clone()));
            }
        }
        ordered.into_iter().collect::<HashMap<_, _>>() // возвращаем в виде HashMap
    }).collect();

    println!("{:?}", ordered_items);
}
