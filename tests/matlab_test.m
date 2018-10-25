% Global
p = 227
g = 182
h = 18 % the hash

r = 91 % Alice random value
k = 78 % Bob random value


alpha = powermod(g, h, p) % compute alpha
a = powermod(alpha, r, p) % compute a
b = powermod(a, k, p) % compute b

inv = modInv(r, ((p-1)/2))

calculate_thing1 = powermod(b, inv, p) % b^1/r
calculate_thing2 = powermod(alpha, k, p) %alpha ^k

function xInv = modInv(x,n)
% ModInv(x,n) computes the multiplicative inverse of x modulo n if one
% exists; errors if no such inverse exists
if gcd(x,n) ~= 1
    error('x has no inverse modulo n')
end

[d, a, b]   = gcd(x,n);
xInv        = mod(a,n);
end
