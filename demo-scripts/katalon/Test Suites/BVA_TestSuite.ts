<?xml version="1.0" encoding="UTF-8"?>
<TestSuiteEntity>
   <description>BVA Test Suite — 12 ca kiểm thử giá trị biên cho bài toán MiniSum (A + B). Test Suite này bind dữ liệu từ file Excel BVA_TestData.xlsx và chạy TC03_BVA_Calculation với mỗi dòng dữ liệu.</description>
   <name>BVA_TestSuite</name>
   <tag></tag>
   <isRerun>false</isRerun>
   <mailRecipient></mailRecipient>
   <numberOfRerun>0</numberOfRerun>
   <pageLoadTimeout>30</pageLoadTimeout>
   <pageLoadTimeoutDefault>true</pageLoadTimeoutDefault>
   <rerunFailedTestCasesOnly>false</rerunFailedTestCasesOnly>
   <rerunImmediately>false</rerunImmediately>
   <testSuiteGuid>e8a7b9c1-4567-4e67-89ab-cdef01234567</testSuiteGuid>
   <testCaseLink>
      <guid>f9b8c0d2-5678-4f78-9abc-def012345678</guid>
      <isReuseDriver>true</isReuseDriver>
      <isRun>true</isRun>
      <testCaseId>Test Cases/TC03_BVA_Calculation</testCaseId>
      <testDataLink>
         <combinationType>ONE</combinationType>
         <id>bva-data-link-01</id>
         <iterationEntity>
            <iterationType>ALL</iterationType>
            <value></value>
         </iterationEntity>
         <testDataId>Data Files/BVA_TestData</testDataId>
      </testDataLink>
      <usingDataBindingAtTestSuiteLevel>true</usingDataBindingAtTestSuiteLevel>
      <variableLink>
         <testDataLinkId>bva-data-link-01</testDataLinkId>
         <type>DATA_COLUMN</type>
         <value>A</value>
         <variableId>var_A</variableId>
      </variableLink>
      <variableLink>
         <testDataLinkId>bva-data-link-01</testDataLinkId>
         <type>DATA_COLUMN</type>
         <value>B</value>
         <variableId>var_B</variableId>
      </variableLink>
      <variableLink>
         <testDataLinkId>bva-data-link-01</testDataLinkId>
         <type>DATA_COLUMN</type>
         <value>Expected</value>
         <variableId>var_Expected</variableId>
      </variableLink>
   </testCaseLink>
</TestSuiteEntity>
