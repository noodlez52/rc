import math

class RCCircuit:
    def __init__(self, R, C):
        self.R = R
        self.C = C

        self.tau = R * C

    def vc(self, t, V0=5):
        return V0 * (1 - math.exp(-t / self.tau))

    def save(self, conn):
        cur = conn.cursor()
        cur.execute("""INSERT INTO rc_data (R, C, tau) VALUES (?, ?, ?)""",
                    (self.R, self.C, self.tau))
        conn.commit()
