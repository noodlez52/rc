import math

class RCCircuit:
    def __init__(self, R, C):
        # resistance
        self.R = R
        # capacitance
        self.C = C

        # How long to reach 63.2$ of the input voltage
        self.tau = R * C
        # How long to reach 99.3% of the input voltage
        self.v0_time = 5 * self.tau

    def vc(self, t, V0=5):
        # the voltage that the capacitor will hold in the give amount of time
        return V0 * (1 - math.exp(-t / self.tau))

    def save(self, conn):
        cur = conn.cursor()
        cur.execute("""INSERT INTO rc_data (R, C, tau) VALUES (?, ?, ?)""",
                    (self.R, self.C, self.tau))
        conn.commit()
