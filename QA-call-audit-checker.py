print("******* QA Call Audit Checker ********")
agent_name = input("Enter agent name: ")
raw_score = int(input("Enter QA score out of 100: "))
kyc_confirmed = input("Did the agent verify customer KYC? (Y/N): ").upper()
pci_compliance_followed = input("Did the agent mask credit card details? (Y/N): ").upper()

if kyc_confirmed == "N" or pci_compliance_followed == "N":
    final_score = 0
    status = "FATAL COMPLIANCE BREACH - REQUIRE TRAINING"

elif raw_score >= 90:
    final_score = raw_score
    status = "PASS - MET CALL - EXCELLENT SERVICE"
elif raw_score >= 80:
    final_score = raw_score
    status = "PASS - MET CALL - MEETS QUALITY STANDARD"
else:
    final_score = raw_score
    status = "FAIL - NOT MET CALL - REQUIRE COACHING"

print(f"Agent: {agent_name} | Final QA Score: {final_score} | Status: {status}")