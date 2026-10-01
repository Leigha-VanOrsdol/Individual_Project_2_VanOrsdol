

class Rotating_CC:
    ALPHA_upper = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    ALPHA_lower = ('a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    
    def RCC_encrypt(self, msg, shift):
        return self.RCC(msg, shift)

    def RCC_decrypt(self, msg, shift):
        # ToDo - delete 'pass' and replace with the correct code to decript.
        # note - the shift parameter is the encryption integer.  
        pass
    
    def RCC (self, msg, shift):
        new_msg = ""
        new_shift = shift
        for ch in msg:
            if ch in self.ALPHA_upper:
                i = self.ALPHA_upper.index(ch)
                ch = self.ALPHA_upper[(i + new_shift)%26]
            if ch in self.ALPHA_lower:
                i = self.ALPHA_lower.index(ch)
                ch = self.ALPHA_lower[(i + new_shift)%26]
            new_shift+=shift
            new_msg += ch
                
        return new_msg


    
    
