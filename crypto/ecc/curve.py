
class curve:
    def __init__(self, A, B, modulus = None): # Curve is y^2 = x^3 + A*x + B
        self.A = A
        self.B = B
        self.modulus = modulus

    def slope(P, Q): # Where P and Q are tuples
        y_diff = P[1]-Q[1]
        x_diff = P[0]-Q[0]
        slope = y_diff/x_diff
        return {"slope":slope, "y_diff":y_diff, "x_diff":x_diff}

    def add(P, Q): # Where P and Q are tuples
        result = self.slope(P,Q)
        xR = ((result.get("slope") * result.get(slope)) % self.modulus) - (P[0]+Q[0])
