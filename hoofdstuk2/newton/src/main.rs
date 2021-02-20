use num::pow::pow;

fn newton(func: impl Fn(f32) -> f32, dfunc: impl Fn(f32) -> f32, x0: f32, epsilon: f32, max_iter: u32) -> Result<f32, String> {
    let mut xn = x0;
    let mut n = max_iter;

    while n != 0  {
        let fxn = func(xn);

        if fxn.abs() < epsilon {
            return Ok(xn);
        }

        // bereken voor volgende iteratie
        let df = dfunc(xn);

        if df == 0.0 { return Err(String::from("Afgeleide wordt 0")); }
        xn = xn - fxn / df;

        n -= 1;
    }

    Err(String::from("Te veel iteraties"))
}

fn main() {
    let p = |x: f32| {pow(x, 3) - pow(x, 2) - 1.0};
    let dp = |x: f32| {3.0*pow(x,2) - 2.0*x};

    let approx = newton(p, dp, 1.0, 1e-10, 10).unwrap();
    println!("Approx: {}", approx);
}
