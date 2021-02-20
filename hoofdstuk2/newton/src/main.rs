use std::time::SystemTime;

use num::pow::pow;

fn newton<T: num::Float>(func: impl Fn(T) -> T, dfunc: impl Fn(T) -> T, x0: T, epsilon: T, max_iter: u32) -> Result<T, String> {
    let mut xn = x0;
    let mut max_iter = max_iter;

    while max_iter != 0  {
        let fxn = func(xn);

        if fxn.abs() < epsilon {
            return Ok(xn);
        }

        // bereken voor volgende iteratie
        let df = dfunc(xn);

        if df == num::zero() { return Err(String::from("Afgeleide wordt 0")); }
        xn = xn - fxn / df;

        max_iter -= 1;
    }

    Err(String::from("Te veel iteraties"))
}

fn main() {
    let start_time = SystemTime::now();

    let p = |x: f64| {pow(x, 3) - pow(x, 2) - 1.0};
    let dp = |x: f64| {3.0*pow(x,2) - 2.0*x};

    let approx = newton(p, dp, 1.0, 1e-10, 10).unwrap();
    println!("Approx: {}", approx);

    println!("Elapsed time: {}", start_time.elapsed().unwrap().as_secs_f64());
}
