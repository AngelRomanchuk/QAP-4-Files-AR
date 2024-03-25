# Description: a program for One Stop Insurance Company to calculate new insurance policy information for its customers.
# Author: Anhelina Romanchuk
# Date(s): Mar 24, 2024
 
 
# Import libraries
import datetime
import FormatValues as FV

# Define progarm constants.
POLICY_NUM = 1944
BASIC_PREM = 869.00
ADD_CAR_DIS = .25
EXTRA_LIAB = 130.00
EXTRA_GLASS = 86.00
EXTRA_LOANER_CAR = 58.00
HST_RATE = .15
PROCESS_FEE = 39.99

TODAY = datetime.datetime.now()

# Define program functions.
def ExtraCost():
    ExtraLibCost = 0
    ExtraGlassCost = 0
    ExtraLoanCost = 0
    if ExtraLiabil == "Y":
        ExtraLibCost = EXTRA_LIAB * NumInsCar
    if GlassCov == "Y":
        ExtraGlassCost = EXTRA_GLASS * NumInsCar
    if LoanerCar == "Y":
        ExtraLoanCost = EXTRA_LOANER_CAR * NumInsCar
    TotExtraCost = ExtraLibCost + ExtraGlassCost + ExtraLoanCost

    return TotExtraCost

def MonthPayCulc():
    if PayMethod == "Down Pay":
        DownPay = TotCost - DownPaySum
        MonPay = (DownPay + PROCESS_FEE) / 8
    else: 
        MonPay = (TotCost + PROCESS_FEE) / 8
    
    return MonPay

def FirstPayDayCulc():
    PayDay = ((TODAY.replace(day=1) + datetime.timedelta(days=34)).replace(day=1))
    return PayDay


# Main program.
while True:

    ProvLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    PayOption = ["Full", "Monthly", "Down Pay"]

    # Gather user input.
    print(f"")
    CustFName = input("Enter the customer first name: ").title()
    CustLName = input("Enter the customer last name:  ").title()
    CustAdd =  input("Enter the customer address: ").title()
    CustCity = input("Enter the customer city:    ").title()

    while True:
        CustProv = input("Enter the customer province (XX): ").upper()
        if CustProv not in ProvLst:
            print("Data Entry Error - invalid province.")
        else:
            break

    CustPostCode = input("Enter the customer postal code: ").upper()
    CustPhoneNum = input("Enter the customer phone number (9999999999): ")
    print(f"")

    NumInsCar = int(input("Enter the number of cars being insured: "))
    ExtraLiabil = input("Enter Y/N for extra liability up to $1,000,000: ").upper()
    GlassCov = input("Enter Y/N for glass coverage: ").upper()
    LoanerCar = input("Enter Y/N for loaner car: ").upper()
    print(f"")

    while True:
        PayMethod = input("Enter the pay method (Full or Monthly or Down Pay): ").title()
        if PayMethod not in PayOption:
            print("Data Entry Error - invalid paymont method.")
        else:
            break
    if PayMethod == "Down Pay":
        DownPaySum = float(input("Enter the amount of down pay: "))
    print(f"")

    ClaimNumList = []
    ClaimDateLst = []
    ClaimAmtLst = []
    while True:
        ClaimNum = input("Enter a claim number ##### (00000 to end): ")
        if ClaimNum == "00000":
            break
        ClaimDateStr = input("Enter a claim date (YYYY-MM-DD): ")
        ClaimDate = datetime.datetime.strptime(ClaimDateStr, "%Y-%m-%d")
        ClaimAmt = float(input("Enter the claim amount: "))
        
        ClaimNumList.append(ClaimNum)
        ClaimDateLst.append(ClaimDate)
        ClaimAmtLst.append(ClaimAmt) 


    # Perform calculations.
    InsPrem = BASIC_PREM + ((NumInsCar - 1) * ADD_CAR_DIS)
    TotExtraCost = ExtraCost()
    TotInsPrem = InsPrem + TotExtraCost
    HST = TotInsPrem * HST_RATE
    TotCost = TotInsPrem + HST

    MonthPay = MonthPayCulc()

    FirstPayDay = FirstPayDayCulc()

    #  Extras msg
    if ExtraLiabil == "Y":
        LiabMsg = "Yes"
    else:
        LiabMsg = "No"
    if GlassCov == "Y":
        GlassMsg = "Yes"
    else:
        GlassMsg = "No"
    if LoanerCar == "Y":
        LoanerMsg = "Yes"
    else:
        LoanerMsg = "No"


    # Display results
    print(f"")
    print(f"")
    print(f"One Stop Insurance Company                       Invoice Date: {FV.FDateS(TODAY):<10s}")
    print(f"Insurance Policy Information                     Total Cars:   {NumInsCar:<2d}")
    print(f"--------------------")
    print(f"Policy Number: {POLICY_NUM:>5d}")
    print(f"--------------------")
    print(f"Customer information: {CustFName[0]:<1s}. {CustLName:<20s} Phone number: {FV.FPhoneNum(CustPhoneNum):<13s}")
    print(f"                      {CustAdd:<30s}")
    CityProvPostC = CustCity + "," + " " + CustProv + " " + CustPostCode
    print(f"                      {CityProvPostC:<30s}")
    print(f"-------------------------------------------------------------------------")
    print(f"All extras added:                      Total Extra Cost:        {FV.FDollar2(TotExtraCost):>9s}")
    print(f"Liability:      {LiabMsg:<3s}                    Total Insurance Premium: {FV.FDollar2(TotInsPrem):>9s}")
    print(f"Glass Coverage: {GlassMsg:<3s}                    HST:                     {FV.FDollar2(HST):>9s}")
    print(f"Loaner:         {LoanerMsg:<3s}                    Total Cost:              {FV.FDollar2(TotCost):>9s}")
    print(f"-------------------------------------------------------------------------")
    print(f"Monthly Payment: {FV.FDollar2(MonthPay):>9s}                 First Payment Date: {FV.FDateS(FirstPayDay):>10s}")
    print(f"")
    print(f"")
    
    # Claim list
    print(f"   Claim #  Claim Date        Amount")
    print(f"   ---------------------------------")
    ClaimIndex = 0
    for Price in ClaimNumList:
        print(f"   {ClaimNumList[ClaimIndex]:>5s}    {FV.FDateS(ClaimDateLst[ClaimIndex]):>10s}    {FV.FDollar2(ClaimAmtLst[ClaimIndex]):>10s}")
        ClaimIndex += 1
    print(f"   ---------------------------------")
    print(f"")
    print(f"---The policy data has been saved---")
    print(f"")
    POLICY_NUM += 1

    # The end of program
    Cont = input("Do you want to continue? (Y/N): ").upper()
    if Cont != "Y" and Cont != "N":
        print("Data Error Entry - answere the question with Y for yes and N for No.")
    elif Cont == "N":
        break

# Any houskiping duties at the end of the program