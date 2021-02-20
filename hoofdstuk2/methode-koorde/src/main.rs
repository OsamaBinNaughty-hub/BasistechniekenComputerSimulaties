use std::time::SystemTime;
use num::pow::pow;

fn koorde<T: num::Float>(func: impl Fn(T) -> T, x0: T, x1: T, epsilon: T, max_iteraties: u32) -> Result<T, String> {
    if x0 == x1 { return Err(String::from("Er is geen verschil tussen x0 en 1"));}
    if epsilon <= num::zero() {return Err(String::from("epsilon mag niet negatief worden"));}

    let mut xnn = x0;
    let mut xn = x1;

    for _ in 0..max_iteraties {
        let fxn = func(xn);
        let fxnn = func(xnn);

        if fxn.abs() < epsilon { return Ok(xn);}

        // Prepare next iteration
        let x = (xn*fxnn - xnn * fxn)/(fxnn - fxn);
        xnn = xn;
        xn = x;
    }

    Err(String::from("Te veel iteraties"))
}

fn main() {
    let start_time = SystemTime::now();

    let p = |x: f64| {pow(x, 3) - pow(x, 2) - 1.0};

    let approx = koorde(p, 1.0, 2.0, 1e-10, 10).unwrap();
    println!("Approx: {}", approx);

    println!("Elapsed time: {}", start_time.elapsed().unwrap().as_secs_f64());
}
