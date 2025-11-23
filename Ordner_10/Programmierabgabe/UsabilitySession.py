# plan: 1. Create class UsabilitySession 2. Add attributes user_id, duration, success, backtracks with init
# 3. Create method is_successful(): return bool, if Session sucessful or not.
# 4. Create methos has_many_backtracks(threshold=2): return True if Backtracks > threshold

class UsabilitySession:
    def __init__(self, user_id, duration, success, backtracks):
        self.user_id = user_id
        self.duration = duration
        self.success = success
        self.backtracks = backtracks

    def is_successful(self): # success muss nicht nochmal mitgegeben werden
        return self.success
        
    def has_many_backtracks(self, backtracks=None):
        if backtracks is not None:
            return backtracks > 2
        
        return self.backtracks > 2