use std::f64::consts::PI;

struct Color {
    color: String,
}

impl Color {
    fn new(color: &str) -> Color {
        Color { color: color.to_string() }
    }
}

enum Shape {
    Rectangle(Rectangle),
    Circle(Circle),
    Square(Square),
}

impl Shape {
    fn get_type(&self) -> &str {
        match self {
            Shape::Rectangle(_) => "Прямоугольник",
            Shape::Circle(_) => "Круг",
            Shape::Square(_) => "Квадрат",
        }
    }

    fn get_area(&self) -> f64 {
        match self {
            Shape::Rectangle(rect) => rect.get_area(),
            Shape::Circle(circle) => circle.get_area(),
            Shape::Square(square) => square.get_area(),
        }
    }
}

struct Rectangle {
    width: f64,
    height: f64,
    color: Color,
}

impl Rectangle {
    fn new(width: f64, height: f64, color: &str) -> Rectangle {
        Rectangle {
            width,
            height,
            color: Color::new(color),
        }
    }

    fn get_area(&self) -> f64 {
        self.width * self.height
    }
}

struct Circle {
    radius: f64,
    color: Color,
}

impl Circle {
    fn new(radius: f64, color: &str) -> Circle {
        Circle {
            radius,
            color: Color::new(color),
        }
    }

    fn get_area(&self) -> f64 {
        PI * self.radius * self.radius
    }
}

struct Square {
    side_length: f64,
    color: Color,
}

impl Square {
    fn new(side_length: f64, color: &str) -> Square {
        Square {
            side_length,
            color: Color::new(color),
        }
    }

    fn get_area(&self) -> f64 {
        self.side_length * self.side_length
    }
}

fn main() {
    let rectangle = Shape::Rectangle(Rectangle::new(5.0, 10.0, "red"));
    let circle = Shape::Circle(Circle::new(3.0, "blue"));
    let square = Shape::Square(Square::new(4.0, "green"));

    println!("Rectangle: {}, Color: {}, Area: {}", rectangle.get_type(), "red", rectangle.get_area());
    println!("Circle: {}, Color: {}, Area: {}", circle.get_type(), "blue", circle.get_area());
    println!("Square: {}, Color: {}, Area: {}", square.get_type(), "green", square.get_area());
}