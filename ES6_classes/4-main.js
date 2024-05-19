import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

const p = new Pricing("a", new Currency("EUR", "Euro"))
console.log(p);
console.log(p.displayFullPrice());