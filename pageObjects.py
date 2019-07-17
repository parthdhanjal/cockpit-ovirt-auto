import os
import time
import logging
import unittest
from datetime import datetime as datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class oVirtDashboardPageObjects():

    URL = ""
    ACCEPT_UNTRUSTED_CERTS = True

    loginUserInput = "login-user-input"
    loginUserInputValue = "root"
    loginPasswordInput = "login-password-input"
    loginPasswordInputValue = ""
    loginButton = "login-button"

    heFrame = 1
    hostedEngineButtonText = "Hosted Engine"

    glusterWizardButton = "//div[@id='content']/div/div/div/div/div/div[3]/span[2]/button"
    glusterWizardButtonText = "Start"

    ThreeNodeDepButton = ".col-sm-3 > .btn"
    ThreeNodeDepButtonText = "Run Gluster Wizard"

    SingleNodeDepButton = ".col-sm-6 > .btn"
    SingleNodeDepButtonText = "Run Gluster Wizard For Single Node"

    host1Input = ".form-horizontal:nth-child(1) > div:nth-child(1) > .form-group .form-control"
    host1InputValue = "h"
    host1Error = "div:nth-child(1) > .form-group .help-block"

    host2Input = ".form-horizontal:nth-child(1) > div:nth-child(2) > .form-group .form-control"
    host2InputValue = "hh"
    host2Error = "div:nth-child(2) > .form-group .help-block"

    host3Input = "div:nth-child(3) > .form-group .form-control"
    host3InputValue = "hhh"
    host3Error = "div:nth-child(3) > .form-group .help-block"

    hostEmptyErrorValue = "Host address cannot be empty"

    wizardNextButton = ".wizard-pf-next"

    handleSameFqdnAsHost = "handleSameFqdnAsHost"
    fqdnAssertBox = ".form-horizontal > .col-md-offset-2"
    fqdnAssertBoxValue = "Provide the address used to add the additional hosts to be managed by Hosted Engine preferrably FQDN or IP address. And both FQDN needs to be added in known_hosts file."

    validFqdn = "10.70.42.231"

    fqdn1Input = "fqdn"
    fqdn1Error = "div:nth-child(1) > .form-group .help-block"

    fqdn2Input = "div:nth-child(2) > .form-group #fqdn"
    fqdn2Error = "div:nth-child(2) > .form-group .help-block"

    fqdnError = ".col-md-6 > .help-block"
    fqdnSameErrorValue = "Both fqdn or ip can not be same."
    fqdnEmptyError = "Please provide fqdn or ip for both hosts."
    fqdnUnreachableError = "Host is not reachable"

    packageAssertBox = ".form-horizontal > .form-group:nth-child(2) > .col-md-2:nth-child(1)"
    packageAssertBoxValue = "Packages"

    addVolumeButton = "strong:nth-child(1)"
    addVolumeButtonValue = "Add Volume"
    EmptyVolumeName = "tr:nth-child(5) > .col-md-3:nth-child(1) .form-control"
    EmptyVolumeNameText = ''
    EmptyVolumeNameValue = "testvol"
    ErrorVolumeName = ".col-md-3:nth-child(1) .help-block"
    ErrorGlusterBrickDirectory = ".col-md-3:nth-child(4) .help-block"
    ErrorVolumeNameValue = "Volume name cannot be empty"
    ErrorGlusterBrickDirectoryValue = "Brick directory cannot be empty"
    deleteVolumeIcon = "tr:nth-child(5) .pficon"

    RaidInformationTitle = ".form-horizontal > .panel-heading > .panel-title"
    RaidInformationTitleText = "Raid Information"
    RaidTypeDropDown = ".col-md-2 .btn"
    RaidTypeDropDownText = "RAID 6"
    RaidTypeDropDownTextAlter = "JBOD"

    device1Input = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(2) .form-control"
    device1InputValue = "/dev/sdb1"

    device2Input = ".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(2) .form-control"
    device2InputValue = "/dev/sdb1"

    device3Input = ".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(2) .form-control"
    device3InputValue = "/dev/sdb1"

    size1Input = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(3) .form-control"
    size1InputValue = "200"

    size2Input = ".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(3) .form-control"
    size2InputValue = "200"

    size3Input = ".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(3) .form-control"
    size3InputValue = "200"

    vdoCheckBox = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(6) > .ansible-wizard-thinp-checkbox"
    h1Size = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(3) .form-control"
    h1VdoSize = ".ansible-wizard-bricks-row:nth-child(2) > .col-md-1:nth-child(7) .form-control"
    h2Size = ".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(3) .form-control"
    h2VdoSize = ".ansible-wizard-bricks-row:nth-child(3) > .col-md-1:nth-child(7) .form-control"
    h3Size = ".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(3) .form-control"
    h3VdoSize = ".ansible-wizard-bricks-row:nth-child(4) > .col-md-1:nth-child(7) .form-control"

    ansibleConfigPreview = ".ansible-wizard-config-preview"
    DeploymentMsg = "div:nth-child(1) > span:nth-child(2)"
    DeploymentMsgText = "Generated Ansible inventory : /etc/ansible/hc_wizard_inventory.yml"

    FinishButton = ".wizard-pf-finish"

    spinner = ".spinner"

    DeploymentMsgSuccess = "div:nth-child(1) > span:nth-child(2)"
    DeploymentMsgSuccessText = "Successfully deployed Gluster"

    DeploymentMsgFail = "div:nth-child(1) > span:nth-child(2)"
    DeploymentMsgFailText = "Deployment failed"

    continueToHostedEngine = ".blank-slate-pf-main-action"
    continueToHostedEngineText = "Continue to Hosted Engine Deployment"
    continueToHostedEngineButtonSelector = ".btn-lg"

    vmFqdnInput = "he-engine-fqdn-input"
    vmFqdnInputValue = ""

    vmFqdnSpinner = ".form-group:nth-child(2) .spinner"
    vmFqdnValidateMsg = "he-validating-engine-fqdn-msg"

    vmFqdnMacAddInput = "he-engine-mac-address-input"
    vmFqdnMacAddInputValue = ""

    vmPasswordInput = "he-cloudinit-root-pwd-input"
    vmPasswordInputValue = "test123"

    heWizardNextButton = ".btn:nth-child(3)"

    hePasswordInput = "he-admin-password-input"
    hePasswordInputValue = "test123"

    prepareVmButton = ".btn:nth-child(4)"
    prepareVmSpinner = ".deployment-status-spinner"

    advanceDropDownText = "Advanced"

    heDiskSizeInput = ".form-group:nth-child(1) > .he-text-with-units > .form-control"
    heDiskSizeInputValue = 70

    heDeploymentButton = ".btn:nth-child(4)"

    def time_sleep(self, sleepTime):
        time.sleep(sleepTime)

    def setupLogFile(self, filename):
        try:
            os.system("mkdir test_logs")
        except:
            print("Directory already exists")
        finally:
            fileName = 'test_logs/'+filename+'.log'
            exists = os.path.isfile(fileName)
            if exists:
                print("Creating backup of existing log file")
                modifiedTime = os.path.getmtime(fileName)
                timestamp = datetime.fromtimestamp(modifiedTime).strftime("%d-%m-%Y_%H:%M:%S")
                os.rename(fileName,fileName+"_"+timestamp)
                print("Created backup file: ", fileName+"_"+timestamp)
                print("Creating log file:", fileName)
                logging.basicConfig(level=logging.DEBUG, filename=fileName, filemode="a", format='%(asctime)s - %(levelname)s - %(message)s')
                logging.info("Starting test %s", fileName)
            else:
                print("No existing log file found, creating log file: ", fileName)
                logging.basicConfig(level=logging.DEBUG, filename=fileName, filemode="a", format='%(asctime)s - %(levelname)s - %(message)s')
                logging.info("Starting test %s", fileName)

    def setup(self):
        try:
            logging.info("Starting Setup")
            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = self.ACCEPT_UNTRUSTED_CERTS
        except:
            logging.error("Unable to setup Profile variables for webdriver")
        try:
            logging.info("Setting up the driver")
            driver = webdriver.Firefox(firefox_profile=profile)
            return driver
        except:
            logging.error("Unable to Setup the driver")

    def open_page(self, driver):
        try:
            logging.info("Opening URL")
            driver.get(self.URL)
        except:
            logging.error("Error opening URL")

    def login(self, driver):
        try:
            logging.info("Waiting for the login page to load")
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.visibility_of_element_located((By.ID, self.loginUserInput)))
        except:
            logging.error("User Login Input element not visible")
        try:
            logging.info("Inputting username")
            loginUserInput = driver.find_element_by_id(self.loginUserInput)
            loginUserInput.send_keys(self.loginUserInputValue)
        except:
            logging.error("User Login Input element not present")
        try:
            logging.info("Inputting password")
            loginPasswordInput = driver.find_element_by_id(self.loginPasswordInput)
            loginPasswordInput.send_keys(self.loginPasswordInputValue)
        except:
            logging.error("User Login Password element not present")
        try:
            logging.info("Clicking on submit")
            loginButton = driver.find_element_by_id(self.loginButton)
            loginButton.click()
        except:
            logging.error("User Login Button element not present")

    def switchFrame(self, driver, frameRef):
        try:
            logging.info("Swtiching frames to %s", frameRef)
            driver.switch_to.frame(frameRef)
        except:
            logging.error("Not able to switch frame. Check if correct frame has been passed as argument")

    def assertHostedEngine(self, driver):
        try:
            logging.info("Asserting Hosted Engine")
            HostedEngine = driver.find_element_by_link_text(self.hostedEngineButtonText)
            assert HostedEngine.text == self.hostedEngineButtonText
            HostedEngine.click()
        except:
            logging.error("Hosted Engine Element not visible")

    def startGlusterDeployment(self, driver):
        try:
            logging.info("Starting Gluster Deployment Wizard")
            GlusterWizard = driver.find_element_by_xpath(self.glusterWizardButton)
            assert GlusterWizard.text == self.glusterWizardButtonText
            GlusterWizard.click()
        except:
            logging.error("Unable to locate Gluster Deployment button")

    def startThreeNodeWizard(self, driver):
        try:
            logging.info("Starting three node deployment")
            ThreeNodeDep = driver.find_element_by_css_selector(self.ThreeNodeDepButton)
            assert ThreeNodeDep.text == self.ThreeNodeDepButtonText
            ThreeNodeDep.click()
        except:
            logging.error("Three Node Deployment Button not found")

    def startSingleNodeWizard(self, driver):
        try:
            logging.info("Starting Single Node Deployment")
            SingleNodeDep = driver.find_element_by_css_selector(self.SingleNodeDepButton)
            assert SingleNodeDep.text == self.SingleNodeDepButtonText
            SingleNodeDep.click()
        except:
            logging.error("Single Node Deployment Button not found")

    def sendHostValuesForThreeNodeDep(self, driver, h1, h2, h3):
        try:
            logging.info("Sending host values for three node deployment")
            driver.find_element_by_css_selector(self.host1Input).send_keys(h1)
            driver.find_element_by_css_selector(self.host2Input).send_keys(h2)
            driver.find_element_by_css_selector(self.host3Input).send_keys(h3)
        except:
            logging.error("Unable to send values to three node deployment")

    def sendHostValuesForSingleNodeDep(self, driver, h1):
        try:
            logging.info("Sending host values for single node deployment")
            driver.find_element_by_css_selector(self.host1Input).send_keys(h1)
        except:
            logging.error("Unable to send values to single node deployment")

    def wizardNextClick(self, driver):
        try:
            logging.info("Clicking Next Button")
            driver.find_element_by_css_selector(self.wizardNextButton).click()
        except:
            logging.error("Error Clicking Next button")

    def fqdnAssertCheck(self, driver):
        try:
            logging.info("FQDN Assert Check")
            fqdnAssert = driver.find_element_by_css_selector(self.fqdnAssertBox)
            assert fqdnAssert.text == self.fqdnAssertBoxValue
        except:
            logging.error("FQDN Assert Check failing")

    def packageAssertCheck(self, driver):
        try:
            logging.info("Package Assert Check")
            packageAssert = driver.find_element_by_css_selector(self.packageAssertBox)
            assert packageAssert.text == self.packageAssertBoxValue
        except:
            logging.error("Package Assert Check failing")

    def volumeAssertCheck(self, driver, click):
        try:
            logging.info("Volume Assert Check")
            AddVolume = driver.find_element_by_css_selector(self.addVolumeButton)
            assert AddVolume.text == self.addVolumeButtonValue
            logging.info("Add volume click %s", click)
            if(click):
                logging.info("Add volume click check")
                AddVolume.click()
        except:
            logging.error("Volume Assert and adding new volume failing")

    def volumeAddCheck(self, driver, volName):
        try:
            logging.info("Volume Add check")
            EmptyVolumeName = driver.find_element_by_css_selector(self.EmptyVolumeName)
            assert EmptyVolumeName.text == self.EmptyVolumeNameText
            EmptyVolumeName.send_keys(volName)
        except:
            logging.error("Volume Add check failing")

    def raidAssertCheck(self, driver):
        try:
            logging.info("Raid Assert Check")
            RaidInformationTitle = driver.find_element_by_css_selector(self.RaidInformationTitle)
            assert RaidInformationTitle.text == self.RaidInformationTitleText
        except:
            logging.error("Raid Assert check failing")

    def raidTypeChange(self, driver, raidType):
        try:
            logging.info("Changing Raid Type")
            RaidTypeDropDown = driver.find_element_by_css_selector(self.RaidTypeDropDown)
            assert RaidTypeDropDown.text == self.RaidTypeDropDownText
            RaidTypeDropDown.click()
            driver.find_element_by_link_text(raidType).click()
            assert RaidTypeDropDown.text == raidType
        except:
            logging.error("Unable to change Raid type")

    def changeBrickDetails(self, driver):
        try:
            logging.info("Changing Brick Details")
            device1 = driver.find_element_by_css_selector(self.device1Input)
            device1.clear()
            device1.send_keys(self.device1InputValue)
            device2 = driver.find_element_by_css_selector(self.device2Input)
            device2.clear()
            device2.send_keys(self.device2InputValue)
            device3 = driver.find_element_by_css_selector(self.device3Input)
            device3.clear()
            device3.send_keys(self.device3InputValue)
            size1 = driver.find_element_by_css_selector(self.size1Input)
            size1.clear()
            size1.send_keys(self.size1InputValue)
            size2 = driver.find_element_by_css_selector(self.size2Input)
            size2.clear()
            size2.send_keys(self.size2InputValue)
            size3 = driver.find_element_by_css_selector(self.size3Input)
            size3.clear()
            size3.send_keys(self.size3InputValue)
        except:
            logging.error("Unable to change brick details")

    def assertPreview(self, driver):
        try:
            logging.info("Preview Assert")
            ansibleConfig = driver.find_element_by_css_selector(self.ansibleConfigPreview)
            logging.info(ansibleConfig.text)
            DeploymentMsg = driver.find_element_by_css_selector(self.DeploymentMsg)
            assert DeploymentMsg.text == self.DeploymentMsgText
        except:
            logging.error("Preview Assert failing")

    def deployGluster(self, driver):
        try:
            logging.info("Clicking Deploy Gluster Button")
            driver.find_element_by_css_selector(self.FinishButton).click()
        except:
            logging.error("Unable to press deploy button")

    def spinnerCheck(self, driver):
        try:
            logging.info("Checking for spinner element")
            spinner = driver.find_element_by_css_selector(self.spinner)
        except:
            logging.error("Unable to find Spinner Element")
        try:
            while spinner.is_displayed():
                logging.info("check: ")
        except:
            logging.error("Element not visible")

    def deploymentSuccessCheck(self, driver):
        try:
            logging.info("Checking for deployment success message")
            DeploymentMsg = driver.find_element_by_css_selector(self.DeploymentMsgSuccess)
            assert DeploymentMsg.text == self.DeploymentMsgSuccessText
        except:
            logging.error("Unable to find deployment fail message")

    def deploymentFailCheck(self, driver):
        try:
            logging.info("Checking for deployment fail message")
            DeploymentMsg = driver.find_element_by_css_selector(self.DeploymentMsgFail)
            assert DeploymentMsg.text == self.DeploymentMsgFailText
        except:
            logging.error("Unable to find deployment fail message")

    def emptyHostAssertCheck(self, driver):
        try:
            logging.info("Asserting Empty Host Validation Check")
            host1 = driver.find_element_by_css_selector(self.host1Error)
            host2 = driver.find_element_by_css_selector(self.host2Error)
            host3 = driver.find_element_by_css_selector(self.host3Error)

            assert host1.text == self.hostEmptyErrorValue
            assert host2.text == self.hostEmptyErrorValue
            assert host3.text == self.hostEmptyErrorValue
        except:
            logging.error("Empty Host validation failing")

    def handleSameFqdnAsHostCheck(self, driver):
        try:
            logging.info("Checking for handle same FQDN button")
            handleSameFqdnAsHostButton = driver.find_element_by_id(self.handleSameFqdnAsHost)
            handleSameFqdnAsHostButton.click()
        except:
            logging.error("Handle Same FQDN check failing")

    def fqdnUnreachableErrorCheck(self, driver):
        try:
            logging.info("FQDN unreachable error check")
            fqdn1_Error = driver.find_element_by_css_selector(self.fqdn1Error)
            fqdn2_Error = driver.find_element_by_css_selector(self.fqdn2Error)

            assert fqdn1_Error.text == self.fqdnUnreachableError
            assert fqdn2_Error.text == self.fqdnUnreachableError
        except:
            logging.error("FQDN unreachable error check failing")

    def fqdnInput(self, driver, fqdn1, fqdn2):
        try:
            logging.info("FQDN Input")
            fqdn1_textArea = driver.find_element_by_id(self.fqdn1Input)
            fqdn1_textArea.send_keys(fqdn1)
            fqdn2_textArea = driver.find_element_by_css_selector(self.fqdn2Input)
            fqdn2_textArea.send_keys(fqdn2)
        except:
            logging.error("Unable to find FQDN input")

    def fqdnSameError(self, driver):
        try:
            logging.info("Checking for same FQDN error")
            fqdnSameError = driver.find_element_by_css_selector(self.fqdnError)
            assert fqdnSameError.text == self.fqdnSameErrorValue
        except:
            logging.error("Unable to check same FQDN error")

    def fqdn2Clear(self, driver):
        try:
            logging.info("Clearing FQDN#2")
            fqdn2_textArea = driver.find_element_by_css_selector(self.fqdn2Input)
            fqdn2_textArea.clear()
        except:
            logging.error("Unable to locate FQDN#2")

    def fqdnEmptyError(self, driver):
        try:
            logging.info("Checking for empty FQDN error")
            fqdnEmptyError = driver.find_element_by_css_selector(self.fqdnError)
            assert fqdnEmptyError.text == self.fqdnEmptyError
        except:
            logging.error("Empty FQDN error assert failing")

    def emptyVolumeCheck(self, driver):
        try:
            logging.info("Checking for empty volume errors")
            assert driver.find_element_by_css_selector(self.ErrorVolumeName).text == self.ErrorVolumeNameValue
            assert driver.find_element_by_css_selector(self.ErrorGlusterBrickDirectory).text == self.ErrorGlusterBrickDirectory
        except:
            logging.error("Empty volume check assert failing")

    def deleteVolumeRow(self, driver, deleteVolume):
        try:
            logging.info("Deleting extra volume row")
            driver.find_element_by_css_selector(deleteVolume).click()
        except:
            logging.error("Unable to locate delete row button")

    def vdoCheck(self, driver):
        try:
            logging.info("Checking for VDO changes")
            vdocheck = driver.find_element_by_css_selector(self.vdoCheckBox)
            vdocheck.click()

            h1Size = driver.find_element_by_css_selector(self.h1Size)
            h1VdoSize = driver.find_element_by_css_selector(self.h1VdoSize)
            assert 10*int(h1Size.get_attribute('value')) == int(h1VdoSize.get_attribute('value'))

            h2Size = driver.find_element_by_css_selector(self.h2Size)
            h2VdoSize = driver.find_element_by_css_selector(self.h2VdoSize)
            assert 10*int(h2Size.get_attribute('value')) == int(h2VdoSize.get_attribute('value'))

            h3Size = driver.find_element_by_css_selector(self.h3Size)
            h3VdoSize = driver.find_element_by_css_selector(self.h3VdoSize)
            assert 10*int(h3Size.get_attribute('value')) == int(h3VdoSize.get_attribute('value'))

        except:
            logging.error("VDO not present")

    def continueToHostedEngineButtonClick(self, driver):
        try:
            logging.info("Checking for successful Gluster Deployment")
            continueToHostedEngine = driver.find_element_by_css_selector(self.continueToHostedEngine)
            assert continueToHostedEngine.text == self.continueToHostedEngineText
        except:
            logging.error("Gluster Deployment not successful")
        try:
            logging.info("Clicking continue to hosted engine button")
            continueToHostedEngineButton = driver.find_element_by_css_selector(self.continueToHostedEngineButtonSelector)
            continueToHostedEngineButton.click()
        except:
            logging.error("Error clicking continue to hosted engine button")

    def addVmFqdn(self, driver):
        try:
            logging.info("Adding a FQDN")
            vmFqdn = driver.find_element_by_id(self.vmFqdnInput)
            vmFqdn.send_keys(self.vmFqdnInputValue)
        except:
            logging.error("Error adding VM FQDN")

    def validateVmFqdn(self, driver):
        try:
            logging.info("Validating VM FQDN")
            vmFqdnSpinner = driver.find_element_by_css_selector(self.vmFqdnSpinner)
        except:
            logging.error("Validating spinner element not found")
        try:
            while vmFqdnSpinner.is_displayed():
                logging.info("check vmFqdnSpinner: ")
        except:
            logging.error("Element not visible")

    def addVmFqdnMacAdd(self, driver):
        try:
            logging.info("Adding VM FQDN MAC address")
            vmFqdnMacAdd = driver.find_element_by_id(self.vmFqdnMacAddInput)
            vmFqdnMacAdd.clear()
            vmFqdnMacAdd.send_keys(self.vmFqdnMacAddInputValue)
        except:
            logging.error("Error adding VM FQDN MAC address")

    def addVmPassword(self, driver):
        try:
            logging.info("Adding VM password")
            vmPassword = driver.find_element_by_id(self.vmPasswordInput)
            vmPassword.send_keys(self.vmPasswordInputValue)
        except:
            logging.error("Error adding VM password")

    def heWizardNextClick(self, driver):
        try:
            logging.info("Clicking Next Button")
            driver.find_element_by_css_selector(self.heWizardNextButton).click()
        except:
            logging.error("Error Clicking Next button")

    def addHePassword(self, driver):
        try:
            logging.info("Adding HE Password")
            hePassword = driver.find_element_by_id(self.hePasswordInput)
            hePassword.send_keys(self.hePasswordInputValue)
        except:
            logging.error("Error adding HE password")

    def prepareVmDeployment(self, driver):
        try:
            logging.info("Preparing VM")
            prepareVm = driver.find_element_by_css_selector(self.prepareVmButton)
            prepareVm.click()
        except:
            logging.error("Error deploying prepare VM script")

    def prepareVmSpinnerCheck(self, driver):
        try:
            logging.info("Checking for spinner element")
            spinner = driver.find_element_by_css_selector(self.prepareVmSpinner)
        except:
            logging.error("Unable to find Spinner Element")
        try:
            while spinner.is_displayed():
                logging.info("check: ")
        except:
            logging.error("Element not visible")

    def changeHeDiskSize(self, driver):
        try:
            logging.info("Changing HE Disk Size")
            advanceDropDown = driver.find_element_by_link_text(self.advanceDropDownText)
            advanceDropDown.click()
            heDiskSize = driver.find_element_by_css_selector(self.heDiskSizeInput)
            heDiskSize.clear()
            heDiskSize.send_keys(self.heDiskSizeInputValue)
        except:
            logging.error("Unable to change HE Disk Size")

    def heDeployment(self, driver):
        try:
            logging.info("Deploying HE")
            heDeploymentButtonClick = driver.find_element_by_css_selector(self.heDeploymentButton)
            heDeploymentButtonClick.click()
        except:
            logging.error("Unable to locate HE deployment button")

    def driver_close(self, driver):
        logging.info("Closing driver and quiting")
        driver.close()
        driver.quit()
