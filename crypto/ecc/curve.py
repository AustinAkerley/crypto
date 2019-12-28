from crypto.src.mod_inv import mod_inv
class curve:
    def __init__(self, A, B, modulus = None): # Curve is y^2 = x^3 + A*x + B
        self.A = A
        self.B = B
        self.modulus = modulus

    def slope(P, Q): # Where P and Q are tuples
        y_diff = (P[1]-Q[1])%self.modulus
        x_diff = (P[0]-Q[0])%self.modulus
        slope = (y_diff * mod_inv(x_diff, self.modulus))%self.modulus
        return {"slope":slope, "y_diff":y_diff, "x_diff":x_diff}

    def add(self, P, Q): # Where P and Q are tuples
        result = self.slope(P,Q)
        slope = result.get("slope")
        xR = ((slope * slope) - ( P[0] + Q[0] )) % self.modulus
        yR = (slope * (P[0] - xR) - P[1]) % self.modulus
