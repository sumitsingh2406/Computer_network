ALGORITHM OF CRC
 	Step 1: START
Step2: INPUT: Dataword, Polynomial
Step3: Convert Polynomial to bits
Step4: Calculate redundancy
Step5: Concatenate dataword and redundancy
Step6: perform Modulo 2 / X-OR division on sender side with dataword and divisor as polynomial bit
Step7: note the Remainder
Step8: Concatenate Remainder of sender to Data word to perform XOR division on Receiver end
Step9: Perform X-OR division on Receiver end
Step 10: Check remainder is 0 or 1
Step 11: If Remainder of Receiver end is 0, then accepted and if 1, then discarded
Step 12: To verify, change any bit of the Dataword and perform Modulo2/X-OR division. If remainer matched with Senders remainder then accepted, if not then Discard
Step 13: STOP

