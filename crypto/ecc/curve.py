from crypto.src.mod_inv import mod_inv
class curve:
    def __init__(self, A, B, modulus = None): # Curve is y^2 = x^3 + A*x + B
        self.A = A
        self.B = B
        self.modulus = modulus

    def slope(P, Q): # Where P and Q are tuples
        y_diff = (P[1]-Q[1])%self.modulus
        x_diff = (P[0]-Q[0])%self.modulus
        slope = y_diff/x_diff
        if isinstance(slope, int):
            return {"slope":slope, "y_diff":y_diff, "x_diff":x_diff}
        else:
            slope = y_diff * mod_inv(x_diff, self.modulus)
            return {"slope":slope, "y_diff":y_diff, "x_diff":x_diff}

    def add(P, Q): # Where P and Q are tuples
        result = self.slope(P,Q)
        slope = result.get("slope")
        xR = ((slope * slope) % self.modulus) - (P[0]+Q[0])
        yR = ((result.get("slope") * result.get("slope")))
