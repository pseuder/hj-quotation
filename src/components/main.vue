<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.toLeft{
    text-align: left;
}
.toCenter{
    text-align: center;
}
.toFlex{
    display:flex;
}
.autoflow{
    overflow: auto;
}
.word-wrap{
    word-wrap: break-word;
}
.control-container {
  position: fixed;
  z-index: 999999;
}
.display-flex {
  display: flex;
}
.tab-body{
    height:75vh; 
    overflow:auto;
}
.tab-footer{
    margin-top:20px; 
    text-align:right;
}
.basic-info{
    font-family: DFKai-sb;
    font-weight: 600;
}
.table-td{
    height: 40px; 
    word-wrap: break-word;
}
.table{
    page-break-after: always;
}
.table:last-child{
    page-break-after: auto;
}
/deep/ .content-wrapper{
    margin: 0 auto;
}
.myModal{
    width: 100%;
    height: 100%;
    position: absolute;
    filter: blur(10px);
    z-index: 10;
    background: #d3d3d3;
    top: 0px;
    left: 0px;
    opacity: .5;
}

.watermark{
    background-size: contain !important;;
    background: url('../assets/watermark.png') no-repeat;
}

</style>

<style>

</style>

<template>
<div style="width: 90%; margin: auto auto">
    <div  v-if="showModal" class="myModal"></div>
    <el-tabs type="border-card" v-model="tabsValue" >
        <el-tab-pane label="設定" name="setting">
            <span slot="label"><i class="el-icon-setting"></i> 設定</span>
            <div class="tab-body">
                <div style="margin: 30px;">
                    <el-button type="warning" style="font-size: 23px; width: 160px;" icon="el-icon-coin"   @click="goBackSide">資料修改</el-button>
                </div>
                <div style="margin: 30px;">
                    <el-button type="danger" style="font-size: 23px; width: 160px;" icon="el-icon-switch-button"   @click="logOut">登出</el-button>
                </div>
            </div>
        </el-tab-pane>
        <el-tab-pane label="基本資料" name="basic">
            <div class="tab-body">
                <el-form label-width="80px">
                    <div style="text-align: left; font-size: 28px;">
                        店家資料
                        <el-button type="info" style="font-size: 18px; padding: 3px;" icon="el-icon-brush" circle @click="clearCompanyForm" size="medium"></el-button>
                    </div>
                    <br>
                    <el-form-item label="店家名稱">
                        <el-input v-model="companyForm.name"></el-input>
                    </el-form-item>
                    <el-form-item label="店家地址">
                        <el-input v-model="companyForm.address"></el-input>
                    </el-form-item>
                    <el-form-item label="店家電話">
                        <el-input v-model="companyForm.telephone"></el-input>
                    </el-form-item>
                    <el-form-item label="店家傳真">
                        <el-input v-model="companyForm.fax"></el-input>
                    </el-form-item>
                    
                    <div style="text-align: left; font-size: 28px;">
                        客戶資料
                        <el-button type="info" style="font-size: 18px; padding: 3px;" icon="el-icon-brush" circle @click="clearClientForm" size="small"></el-button>
                    </div>
                    <br>
                    <el-form-item label="客戶名稱">
                        <el-input v-model="clientForm.name"></el-input>
                    </el-form-item>
                    <el-form-item label="客戶地址">
                        <el-input v-model="clientForm.address"></el-input>
                    </el-form-item>
                    <el-form-item label="客戶電話">
                        <el-input v-model="clientForm.telephone"></el-input>
                    </el-form-item>
                    <el-form-item label="客戶傳真">
                        <el-input v-model="clientForm.fax"></el-input>
                    </el-form-item>
                    <el-form-item label="客戶信箱">
                        <el-input v-model="clientForm.email"></el-input>
                    </el-form-item>
                    <el-form-item label="日期">
                        <div style="width:100%; text-align: left;">
                            <el-date-picker
                                v-model="clientForm.date"
                                align="right"
                                type="date"
                                placeholder="選擇日期"
                                :picker-options="pickerOptions" />
                        <div>
                    </el-form-item>
                    
                </el-form>
            </div>
            <div style="" class="tab-footer">
                <el-button type="primary" @click="changeTab('service')">下一步</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="服務項目" name="service">
            <div class="tab-body">
                <div style="text-align: left; font-size: 28px;">
                    新增服務項目
                    <el-button type="info" style="font-size: 18px; padding: 3px;" icon="el-icon-brush" circle @click="clearServiceTable" size="small"></el-button>
                </div>
                <el-table :data="serviceTable" empty-text="尚無資料">
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button size="mini" type="danger" icon="el-icon-delete" circle @click="deleteService(scope.$index, scope.row)"></el-button>
                        </template>
                    </el-table-column>
                    <el-table-column label="規格" prop="specification"></el-table-column>
                    <el-table-column label="數量" prop="number"></el-table-column>
                    <el-table-column label="單位" prop="unit"></el-table-column>
                    <el-table-column label="單價" prop="unitPrice"></el-table-column>
                    <el-table-column label="金額" prop="price"></el-table-column>
                    <el-table-column label="備註" prop="remark"></el-table-column>
                </el-table>
                <el-button type="warning" icon="el-icon-plus" circle @click="openSpecificationDialog"></el-button>
            </div>
            <div class="tab-footer">
                <el-button type="primary" @click="changeTab('basic')" plain>上一步</el-button>
                <el-button type="primary" @click="changeTab('other')">下一步</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="其他項目" name="other">
            <div class="tab-body">
                <div style="text-align: left; font-size: 28px;">
                    新增其他項目
                    <el-button type="info" style="font-size: 18px; padding: 3px;" icon="el-icon-brush" circle @click="clearOtherTable" size="small"></el-button>
                </div>
                <el-table :data="otherTable" empty-text="尚無資料">
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button size="mini" type="danger" icon="el-icon-delete" circle @click="deleteOther(scope.$index, scope.row)"></el-button>
                        </template>
                    </el-table-column>
                    <el-table-column label="規格" prop="specification"></el-table-column>
                    <el-table-column label="數量" prop="number"></el-table-column>
                    <el-table-column label="單位" prop="unit"></el-table-column>
                    <el-table-column label="單價" prop="unitPrice"></el-table-column>
                    <el-table-column label="金額" prop="price"></el-table-column>
                    <el-table-column label="備註" prop="remark"></el-table-column>
                </el-table>
                <el-button type="warning" icon="el-icon-plus" circle @click="openOtherDialog"></el-button>
            </div>
            <div class="tab-footer">
                <el-button type="primary" @click="changeTab('service')" plain>上一步</el-button>
                <el-button type="primary" @click="changeTab('attachment')">下一步</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="附件" name="attachment">
            <div class="tab-body">
                <div style="text-align: left; font-size: 28px;">
                    新增附件
                    <el-button type="info" style="font-size: 18px; padding: 3px;" icon="el-icon-brush" circle @click="clearAttachmentTable" size="small"></el-button>
                </div>
                <el-table :data="attachmentTable" empty-text="尚無資料">
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button size="mini" type="danger" icon="el-icon-delete" circle @click="deleteAttachment(scope.$index, scope.row)"></el-button>
                        </template>
                    </el-table-column>
                    <el-table-column label="附件名稱" prop="name"></el-table-column>
                    <el-table-column label="備註" prop="remark"></el-table-column>
                </el-table>
                <el-button type="warning" icon="el-icon-plus" circle @click="openAttachmentDialog"></el-button>
            </div>
            <div class="tab-footer">
                <el-button type="primary" @click="changeTab('other')" plain>上一步</el-button>
                <el-button type="primary" @click="changeTab('finish')">下一步</el-button>
            </div>
        </el-tab-pane>

        <el-tab-pane label="完成" name="finish">
            <div class="tab-body">
                
                <div style="height:auto; width: 96%; max-width: 675px; border: black double 6px; margin: auto">
                    <div style="position:relative">
                        <div>
                            <div style="" class="basic-info">
                                <div style="text-align:center; font-size: 35px;">報   價   單</div>
                                <div style="" class="toLeft">{{companyForm.name}}</div>
                                <div style="" class="toLeft">{{companyForm.address}}</div>
                                <div style="" class="toFlex">
                                    <div style="">TEL：{{companyForm.telephone}}</div>
                                    <div style="margin-left:20px">FAX：{{companyForm.fax}}</div>
                                </div>
                                <br>
                                <div style="" class="toFlex">
                                    <div style="width:60%" class="toLeft">客戶名稱：{{clientForm.name}}</div>
                                    <div style="" class="toLeft">日期：{{clientForm.date.toLocaleDateString()}}</div>
                                </div>
                                <div style="" class="toFlex">
                                    <div style="width:60%" class="toLeft">聯絡電話：{{clientForm.telephone}}</div>
                                    <div style="" class="toLeft">傳真：{{clientForm.fax}}</div>
                                </div>
                                <div style="" class="toLeft">地址：{{clientForm.address}}</div>
                                <div style="" class="toLeft">Email：{{clientForm.email}}</div>
                            </div>
                            <table border style="border-collapse:collapse; width:100%; font-family: PMingLiU;">
                                <tr style="">
                                    <th width="45%" class="table-td">品名</th>
                                    <th width="6%"  class="table-td">數量</th>
                                    <th width="6%"  class="table-td">單位</th>
                                    <th width="13%" class="table-td">單價</th>
                                    <th width="13%" class="table-td">金額</th>
                                    <th width="17%" class="table-td">備註</th>
                                </tr>
                                <tr v-for="item in serviceTable" :key="item">
                                    <td style="max-width: 45%; text-align:left;" class="table-td">{{item.specification}}</td>
                                    <td style="max-width: 6%; text-align:center;" class="table-td">{{item.number}}</td>
                                    <td style="max-width: 6%; text-align:center;" class="table-td">{{item.unit}}</td>
                                    <td style="max-width: 13%; text-align:right;" class="table-td">
                                        <div style="margin-right: 4px;">${{item.unitPrice}}</div>
                                    </td>
                                    <td style="max-width: 13%; text-align:right;" class="table-td">
                                        <div style="margin-right: 4px;">${{item.price}}</div>
                                    </td>
                                    <td style="max-width: 17%; text-align:center;" class="table-td">{{item.remark}}</td>
                                </tr>
                                <tr v-for="item in otherTable" :key="item">
                                    <td style="max-width: 45%; text-align:left;" class="table-td">{{item.specification}}</td>
                                    <td style="max-width: 6%; text-align:center;" class="table-td">{{item.number}}</td>
                                    <td style="max-width: 6%; text-align:center;" class="table-td">{{item.unit}}</td>
                                    <td style="max-width: 13%; text-align:right;" class="table-td">
                                        <div style="margin-right: 4px;">${{item.unitPrice}}</div>
                                    </td>
                                    <td style="max-width: 13%; text-align:right;" class="table-td">
                                        <div style="margin-right: 4px;">${{item.price}}</div>
                                    </td>
                                    <td style="max-width: 17%; text-align:center;" class="table-td">{{item.remark}}</td>
                                </tr>
                                <tr v-for="item in attachmentTable" :key="item">
                                    <td style="text-align:left;" class="table-td" colspan="5">{{item.name}}</td>
                                    <td style="text-align:left;" class="table-td" >{{item.remark}}</td>
                                </tr>
                                <tr v-for="item of 11-(serviceTable.length+otherTable.length+attachmentTable.length)" :key="item">
                                    <td v-for="item of 6" :key="item" class="table-td"></td>
                                </tr>
                                <tr>
                                    <td class="toLeft table-td">
                                        <div style="display:flex">
                                            <div style="width: 40%; margin: auto;">施工日期:</div>
                                            <el-input v-model="constructionDate"></el-input>
                                        </div>
                                    </td>
                                    <td v-for="item of 5" :key="item" class="table-td"></td>
                                </tr>
                                <tr>
                                    <td colspan="6" class="toLeft table-td">
                                        <div style="display:flex">
                                            <div style="width:30%; display:flex">
                                                <div style="width: 24%; margin: auto;">訂金:</div>
                                                <el-input v-model="deposit" style="margin: auto;" />
                                            </div>
                                            <div style="width:40%; display:flex">
                                                <div style="width: 48%; margin: auto;">機器設備款:</div>
                                                <el-input v-model="machineEquipment" style="margin: auto;" />
                                            </div>
                                            <div style="width:30%; display:flex">
                                                <div style="width: 37%; margin: auto;">完成款:</div>
                                                <el-input v-model="completedPayment" style="margin: auto;" />
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="letter-spacing: 32px; text-align:center" class="table-td">合計</td>
                                    <td colspan="5" style="text-align:center" class="table-td">${{allPrice}}</td>
                                </tr>
                            </table>
                        </div>
                        <div style="height: 100px">
                            <div style="height:100%; " class="toLeft toFlex basic-info">
                                <div style="margin:auto; width: 25%">和進電器水電行:</div>
                                <div style="width: 25%;" class="watermark"></div>
                                <div style="margin:auto; width: 20%">客戶簽名:</div>
                                <div style="width: 30%; z-index: 2;">
                                    <div v-if="clientSignImg==''" style="width: 100%; height: 98%;"  @click="signCanvasVisible=true; showModal=false" />
                                    <img v-else :src=clientSignImg style="width: 100%; height: 98%;" @click="signCanvasVisible=true; showModal=false" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="tab-footer">
                <el-button type="primary" @click="changeTab('other')" plain>上一步</el-button>
                <el-button type="primary" @click="generateReport">下載PDF</el-button>
            </div>
        </el-tab-pane>
    </el-tabs>
    
    <el-dialog title="選擇空調設備規格" :visible.sync="specificationDialogVisible" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false"  :show-close="false">
        <div style="height: 55vh; overflow-y: auto; overflow-x: hidden;" ref="specificationDialog">
            <el-form :model="addSpecificationForm" >
                <el-form-item label="品牌">
                    <el-select v-model="addSpecificationValue.brand" placeholder="選擇品牌" style="width:100%" @change="selectChange('brand')">
                        <el-option
                            v-for="item in addSpecificationOption.brand"
                            :key="item"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="種類">
                    <el-select v-model="addSpecificationValue.category" placeholder="選擇種類" style="width:100%" @change="selectChange('category')" name="categorySelect">
                        <el-option
                            v-for="item in addSpecificationOption.category"
                            :key="item"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="商品">
                    <el-select v-model="addSpecificationValue.name" placeholder="選擇商品" style="width:100%" name="nameSelect" @change="selectChange('name')">
                        <el-option
                            v-for="item in addSpecificationOption.name"
                            :key="item"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="數量">
                    <el-input v-model="addSpecificationValue.number" placeholder="輸入數量"></el-input>
                </el-form-item>
                <el-form-item label="單位">
                    <el-select v-model="addSpecificationValue.unit" placeholder="選擇單位" style="width: 100%;">
                        <el-option v-for="item in defaultUnit" :key="item.id" :label="item.name" :value="item.name" >
                            <div v-if="item.name=='other'" @click.stop="">
                                <span>自訂單位：</span>
                                <input v-model="addSpecificationValue.unit" placeholder="輸入單位" style="border-width: 0px 0px 1px 0px; width: 20vw;" />
                            </div>
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="單價">
                    <el-input v-model="addSpecificationValue.unitPrice" placeholder="輸入單價"></el-input>
                </el-form-item>
                <el-form-item label="備註">
                    <el-input v-model="addSpecificationValue.remark" placeholder="輸入備註"></el-input>
                </el-form-item>
            </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
            <el-button type="warning" plain @click="openSpecificationDialog">清空</el-button>
            <el-button type="primary" plain @click="specificationDialogVisible=false; showModal=false">取 消</el-button>
            <el-button type="primary" @click="addService">確 定</el-button>
        </span>
    </el-dialog>

    <el-dialog title="輸入其他服務" :visible.sync="otherDialogVisible" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
        <div style="height: 55vh; overflow-y: auto; overflow-x: hidden;">
            <el-form :model="addOtherValue" >
                <el-form-item label="選擇服務名稱">
                    <el-select v-model="addOtherValue.specification" placeholder="服務名稱" style="width: 100%;" @change="selectChange('service')">
                        <el-option v-for="item in addOtherOption" :key="item.name" :label="item.name" :value="item.name">
                            <div v-if="item.name=='other'" @click.stop="">
                                <span>自訂服務名稱：</span>
                                <input v-model="addOtherValue.specification" placeholder="輸入服務名稱" style="border-width: 0px 0px 1px 0px; width: 20vw;" />
                            </div>
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="數量">
                    <el-input v-model="addOtherValue.number" placeholder="輸入數量"></el-input>
                </el-form-item>
                <el-form-item label="單位">
                    <el-select v-model="addOtherValue.unit" placeholder="選擇單位" style="width: 100%;">
                        <el-option v-for="item in defaultUnit" :key="item.id" :label="item.name" :value="item.name" >
                            <div v-if="item.name=='other'" @click.stop="">
                                <span>自訂單位：</span>
                                <input v-model="addOtherValue.unit" placeholder="輸入單位" style="border-width: 0px 0px 1px 0px; width: 20vw;" />
                            </div>
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="單價">
                    <el-input v-model="addOtherValue.unitPrice" placeholder="輸入單價"></el-input>
                </el-form-item>
                <el-form-item label="備註">
                    <el-input v-model="addOtherValue.remark" placeholder="輸入備註"></el-input>
                </el-form-item>
            </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
            <el-button type="warning" plain @click="openOtherDialog">清空</el-button>
            <el-button type="primary" plain @click="otherDialogVisible = false; showModal=false">取 消</el-button>
            <el-button type="primary" @click="addOther">確 定</el-button>
        </span>
    </el-dialog>

    <el-dialog title="輸入附件" :visible.sync="attachmentDialogVisible" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
        <div style="height: 55vh; overflow-y: auto; overflow-x: hidden;">
            <el-form :model="addAttachValue" >
                <el-form-item label="附件名稱">
                    <el-select v-model="addAttachValue.name" placeholder="服務名稱" style="width: 100%;" @change="selectChange('attachment')">
                        <el-option v-for="item in addAttachOption" :key="item.name" :label="item.name" :value="item.name">
                            <div v-if="item.name=='other'" @click.stop="">
                                <span>自訂附件名稱：</span>
                                <input v-model="addAttachValue.name" placeholder="輸入附件名稱" style="border-width: 0px 0px 1px 0px; width: 20vw;" />
                            </div>
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="附件備註">
                    <el-input v-model="addAttachValue.remark"  />
                </el-form-item>
            </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
            <el-button type="warning" plain @click="openAttachmentDialog">清空</el-button>
            <el-button type="primary" plain @click="attachmentDialogVisible = false; showModal=false">取 消</el-button>
            <el-button type="primary" @click="addAttach">確 定</el-button>
        </span>
    </el-dialog>

    <el-dialog title="客戶簽名" :visible.sync="signCanvasVisible" :close-on-click-modal="false" width="80%" :modal="false" :close-on-press-escape="false" :show-close="false">
        <div>
            <vue-esign 
                ref="esign" 
                :width="1000" 
                :height="500" 
                :isCrop="isCrop" 
                :lineWidth="lineWidth" 
                :lineColor="lineColor" 
                :bgColor.sync="bgColor"
                style="borderStyle: double; borderColor: black;"
            />
            <div style="margin-top:20px; text-align:right">
                <el-button type="warning" plain @click="$refs.esign.reset()">清除</el-button>
                <el-button type="primary" plain @click="signCanvasVisible=false; showModal=false">取消</el-button>
                <el-button type="primary" @click="handleGenerate">確定</el-button>
            </div>
        </div>
    </el-dialog>







    <!-- PDF實際下載根據，不顯示 -->
    <vue-html2pdf
        :show-layout="false"
        :float-layout="false"
        :enable-download="true"
        :preview-modal="false"
        :paginate-elements-by-height="1400"
        filename="我是pdf"
        :pdf-quality="2"
        :manual-pagination="true"
        pdf-format="a4"
        pdf-orientation="landscape"
        pdf-content-width="800px"
        :html-to-pdf-options="htmlToPdfOptions"
        @hasStartedGeneration="hasStartedGeneration()"
        @hasGenerated="hasGenerated($event)"
        ref="html2Pdf"
        id="html2Pdf"
        style="display:none">
    >
    <section slot="pdf-content">
        <div style="height:auto; width: 96%; max-width: 675px; border: black double 6px; margin: 20px auto">
            <div style="position:relative">
                <div class="watermark" />
                <div>
                    <div style="" class="basic-info">
                        <br>
                        <div style="text-align:center; font-size: 35px;">報   價   單</div>
                        <div style="" class="toLeft">{{companyForm.name}}</div>
                        <div style="" class="toLeft">{{companyForm.address}}</div>
                        <div style="" class="toFlex">
                            <div style="">TEL：{{companyForm.telephone}}</div>
                            <div style="margin-left:20px">FAX：{{companyForm.fax}}</div>
                        </div>
                        <br>
                        <div style="" class="toFlex">
                            <div style="width:60%" class="toLeft">客戶名稱：{{clientForm.name}}</div>
                            <div style="" class="toLeft">日期：{{clientForm.date.toLocaleDateString()}}</div>
                        </div>
                        <div style="" class="toFlex">
                            <div style="width:60%" class="toLeft">聯絡電話：{{clientForm.telephone}}</div>
                            <div style="" class="toLeft">傳真：{{clientForm.fax}}</div>
                        </div>
                        <div style="" class="toLeft">地址：{{clientForm.address}}</div>
                        <div style="" class="toLeft">Email：{{clientForm.email}}</div>
                    </div>
                    <table border style="border-collapse:collapse; width:100%; font-family: PMingLiU;">
                        <tr style="">
                            <th width="45%" class="table-td">品名</th>
                            <th width="6%"  class="table-td">數量</th>
                            <th width="6%"  class="table-td">單位</th>
                            <th width="13%" class="table-td">單價</th>
                            <th width="13%" class="table-td">金額</th>
                            <th width="17%" class="table-td">備註</th>
                        </tr>
                        <tr v-for="item in serviceTable" :key="item">
                            <td style="max-width: 45%; text-align:left;" class="table-td">{{item.specification}}</td>
                            <td style="max-width: 6%; text-align:center;" class="table-td">{{item.number}}</td>
                            <td style="max-width: 6%; text-align:center;" class="table-td">{{item.unit}}</td>
                            <td style="max-width: 13%; text-align:right;" class="table-td">
                                <div style="margin-right: 4px;">${{item.unitPrice}}</div>
                            </td>
                            <td style="max-width: 13%; text-align:right;" class="table-td">
                                <div style="margin-right: 4px;">${{item.price}}</div>
                            </td>
                            <td style="max-width: 17%; text-align:center;" class="table-td">{{item.remark}}</td>
                        </tr>
                        <tr v-for="item in otherTable" :key="item">
                            <td style="max-width: 45%; text-align:left;" class="table-td">{{item.specification}}</td>
                            <td style="max-width: 6%; text-align:center;" class="table-td">{{item.number}}</td>
                            <td style="max-width: 6%; text-align:center;" class="table-td">{{item.unit}}</td>
                            <td style="max-width: 13%; text-align:right;" class="table-td">
                                <div style="margin-right: 4px;">${{item.unitPrice}}</div>
                            </td>
                            <td style="max-width: 13%; text-align:right;" class="table-td">
                                <div style="margin-right: 4px;">${{item.price}}</div>
                            </td>
                            <td style="max-width: 17%; text-align:center;" class="table-td">{{item.remark}}</td>
                        </tr>
                        <tr v-for="item in attachmentTable" :key="item">
                            <td style="text-align:left;" class="table-td" colspan="5">{{item.name}}</td>
                            <td style="text-align:left;" class="table-td" >{{item.remark}}</td>
                        </tr>
                        <tr v-for="item of 11-(serviceTable.length+otherTable.length+attachmentTable.length)" :key="item">
                            <td v-for="item of 6" :key="item" class="table-td"></td>
                        </tr>
                        <tr>
                            <td class="toLeft table-td">
                                施工日期：{{constructionDate}}
                            </td>
                            <td v-for="item of 5" :key="item" class="table-td"></td>
                        </tr>
                        <tr>
                            <td colspan="6" class="toLeft table-td">
                                <div style="display:flex">
                                    <div style="width:30%;">
                                        訂金：{{deposit}}
                                    </div>
                                    <div style="width:40%;">
                                        機器設備款：{{machineEquipment}}
                                    </div>
                                    <div style="width:30%;">
                                        完成款：{{completedPayment}}
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td style="letter-spacing: 32px; text-align:center" class="table-td">合計</td>
                            <td colspan="5" style="text-align:center" class="table-td">${{allPrice}}</td>
                        </tr>
                    </table>
                </div>
                <div style="height: 100px">
                    <div style="height:100%; " class="toLeft toFlex basic-info">
                        <div style="margin:auto; width: 25%">和進電器水電行:</div>
                        <div style="width: 25%;" class="watermark"></div>
                        <div style="margin:auto; width: 20%">客戶簽名:</div>
                        <div style="width: 30%;">
                            <div v-if="clientSignImg==''" style="width: 100%; height: 98%;" />
                            <img v-else :src=clientSignImg style="width: 100%; height: 98%;" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    </vue-html2pdf>

</div>
</template>

<script>

import vueEsign from 'vue-esign'
import VueHtml2pdf from 'vue-html2pdf'
export default {
  name: 'Main',
  components: {
    vueEsign,
    VueHtml2pdf
  },
  data: function() {
        return {
            tabsValue:'basic',
            companyForm:{
                name:'和進電器水電行',
                address:'新竹縣新豐鄉建興路一段154-8號',
                telephone:'03-5576567',
                fax:'03-573526',
            },
            clientForm:{
                name:'',
                address:'',
                telephone:'',
                fax:'',
                email:'',
                date:'',
            },
            serviceTable:[],
            specificationDialogVisible: false,
            addSpecificationOption:{
                brand:[],
                category:[],
                name:[],
            },
            addSpecificationValue:{
                brand:'',
                category:'',
                name:'',
                number:'1',
                unit:'',
                unitPrice:'',
                remark:'',
            },
            otherTable:[],
            otherDialogVisible: false,
            addOtherOption:[],
            addOtherValue:{
                specification:'',
                number:'1',
                unit:'',
                unitPrice:'0',
                remark:'',
            },
            allProduct:[],
            clientSignImg: '',
            signCanvasVisible: false,

            attachmentDialogVisible: false,
            attachmentTable:[],
            addAttachOption:[],
            addAttachValue:{
                name:'',
                remark:'',
            },

            name: 'Vue.js',
            showModal: false,
            constructionDate: '',
            deposit: '',
            machineEquipment: '',
            completedPayment: '',
            defaultUnit: [],
        }
  },
  created(){
    if(sessionStorage.getItem("login")!='true'){
        let self = this;
        self.$message({message: '登入會期已過，請重新登入!', type: 'warning'})
        setTimeout(() => {
            self.$router.push({name: 'login'});
        }, 3000);
    }
    else{
        let self = this
        this.axios.get('getProduct')
        .then((response)=>{
            self.allProduct = response.data;
            let brandSet = new Set();
            self.allProduct.forEach(function(item){
                brandSet.add(item.brand)
            })
            self.addSpecificationOption.brand = [...brandSet];
        })

        this.axios.get('getOther')
        .then((response)=>{
            self.addOtherOption = response.data
            self.addOtherOption.push({name:'other'})
        })

        this.axios.get('getAttachment')
        .then((response)=>{
            self.addAttachOption = response.data
            self.addAttachOption.push({name:'other'})
        })

        this.axios.get('getUnit').then(res => {
            self.defaultUnit = res.data;
            self.defaultUnit.push({id:9999, name:'other'})
        })

        this.clientForm.date = new Date();


    }
  },
  computed: {
    htmlToPdfOptions() {
      return {
        margin: 0,
        filename: "報價單.pdf",
        image: {
          type: "jpeg",
          quality: 0.98,
        },
        enableLinks: true,
        html2canvas: {
          scale: 2,
          useCORS: true,
        },
        jsPDF: {
          unit: "in",
          format: 'a4',
          orientation: 'portrait',
        },
      };
    },
    allPrice(){
        let allPrice = 0;
        this.serviceTable.forEach(function(item){
            allPrice += Number(String(item.price).replaceAll(',', ''))
        })
        this.otherTable.forEach(function(item){
            allPrice += Number(String(item.price).replaceAll(',', ''))
        })
        return allPrice.toLocaleString();
    }
  },
  methods:{
    changeTab(destination){
        this.tabsValue = destination
    },
    deleteService(index, row){
        this.serviceTable.splice(index, 1)
    },
    deleteOther(index, row){
        this.otherTable.splice(index, 1)
    },
    selectChange(source){
        if(source == 'brand'){
            let self = this;
            let categorySet = new Set();
            self.allProduct.forEach(function(item){
                if(item.brand == self.addSpecificationValue.brand){
                    categorySet.add(item.category)
                }
            })
            self.addSpecificationOption.category = [...categorySet];
            
            document.getElementsByName('categorySelect')[0].click()
        }
        else if(source == 'category'){
            let self = this;
            let productSet = new Set();
            self.allProduct.forEach(function(item){
                if(item.brand == self.addSpecificationValue.brand && item.category == self.addSpecificationValue.category){
                    productSet.add(item.name)
                }
            })
            self.addSpecificationOption.name = [...productSet];
            document.getElementsByName('nameSelect')[0].click()
        }
        else if(source == 'name'){
            let self = this;
            let product = self.allProduct.find(function(item){
                return item.brand == self.addSpecificationValue.brand && item.category == self.addSpecificationValue.category && item.name == self.addSpecificationValue.name;
            })
            self.addSpecificationValue.unitPrice = product.unitPrice;
        }
        else if(source == 'service'){
            let self = this;
            let product = self.addOtherOption.find(function(item){
                return item.name == self.addOtherValue.specification;
            })
            self.addOtherValue.unitPrice = product.unitPrice;
        }
        else if(source == 'attachment'){
            let self = this;
            let product = self.addAttachOption.find(function(item){
                return item.name == self.addAttachValue.name;
            })
            self.addAttachValue.remark = product.remark;
        }
    },
    openSpecificationDialog(){
        this.addSpecificationValue.brand = '';
        this.addSpecificationValue.category = '';
        this.addSpecificationValue.name = '';
        this.addSpecificationValue.number = '1';
        this.addSpecificationValue.unit = '';
        this.addSpecificationValue.unitPrice = '';
        this.addSpecificationValue.remark = '';
        this.addSpecificationOption.category = [];
        this.addSpecificationOption.name = [];
        this.specificationDialogVisible = true;
        this.showModal = true;
        let self = this
        setTimeout(() => {
            self.$refs.specificationDialog.scrollTop=0
        }, 50);
        
    },
    addService(){
        if(this.serviceTable.length + this.otherTable.length + this.attachmentTable.length >= 10){
            this.$message({message: '服務項目+其他服務+附件不得超過11項!', type: 'warning'})
            return;
        }
        //只能填寫數字
        if(!this.addSpecificationValue.number.match(/^[0-9]*$/)){
            this.$message({message: '數量只能填寫數字!', type: 'warning'})
            return;
        }
        //只能填寫數字和逗號
        if(!this.addSpecificationValue.unitPrice.match(/^[0-9,]*$/)){
            this.$message({message: '單價只能填寫數字和逗號!', type: 'warning'})
            return;
        }

        let fullSpecification = this.addSpecificationValue.brand + this.addSpecificationValue.category + this.addSpecificationValue.name;
        let totalPrice = (Number(this.addSpecificationValue.number) * Number(this.addSpecificationValue.unitPrice.replaceAll(',', ''))).toLocaleString();
        this.serviceTable.push({
            specification: fullSpecification,
            number: this.addSpecificationValue.number,
            unit: this.addSpecificationValue.unit,
            unitPrice: this.addSpecificationValue.unitPrice,
            price: totalPrice,
            remark: this.addSpecificationValue.remark,
        })
        this.specificationDialogVisible = false;
        this.showModal=false
    },
    handleGenerate () {
        let self = this;
        self.$refs.esign.generate().then(res => {
            self.clientSignImg = res
            self.signCanvasVisible = false
        }).catch(err => {
            self.$message({message: '沒有偵測到簽名!', type: 'error'})
        })
    },
    generateReport () {
      this.$refs.html2Pdf.generatePdf()
    },
    goBackSide(){
        this.$router.push({name: 'backSide'});
    },
    logOut(){
        sessionStorage.clear();
        this.$router.push({name: 'login'});
    },
    clearCompanyForm(){
        this.companyForm.name = '';
        this.companyForm.address = '';
        this.companyForm.telephone = '';
        this.companyForm.fax = '';
    },
    clearClientForm(){
        this.clientForm.name = '';
        this.clientForm.address = '';
        this.clientForm.telephone = '';
        this.clientForm.fax = '';
        this.clientForm.email = '';
        this.clientForm.date = new Date();
    },
    clearServiceTable(){
        this.serviceTable = [];
    },
    openOtherDialog(){
        this.addOtherValue.specification = '';
        this.addOtherValue.number = '1';
        this.addOtherValue.unit = '';
        this.addOtherValue.unitPrice = '0';
        this.addOtherValue.remark = '';
        this.showModal=true
        this.otherDialogVisible = true;
    },
    clearAttachmentTable(){
        this.attachmentTable = [];
    },
    openAttachmentDialog(){
        this.addAttachValue.name = '';
        this.addAttachValue.remark = '';
        this.showModal=true
        this.attachmentDialogVisible = true;
    },
    deleteAttachment(index){
        this.attachmentTable.splice(index, 1)
    },
    addAttach(){
        if(this.serviceTable.length + this.otherTable.length + this.attachmentTable.length >= 10){
            this.$message({message: '服務項目+其他服務+附件不得超過11項!', type: 'warning'})
            return;
        }
        this.attachmentTable.push({
            name: this.addAttachValue.name,
            remark: this.addAttachValue.remark,
        })
        this.attachmentDialogVisible = false;
        this.showModal=false
    },
    addOther(){
        if(this.serviceTable.length + this.otherTable.length + this.attachmentTable.length >= 10){
            this.$message({message: '服務項目+其他服務+附件不得超過11項!', type: 'warning'})
            return;
        }
        //只能填寫數字
        if(!this.addOtherValue.number.match(/^[0-9]*$/)){
            this.$message({message: '數量只能填寫數字!', type: 'warning'})
            return;
        }
        //只能填寫數字和逗號
        if(!this.addOtherValue.unitPrice.match(/^[0-9,]*$/)){
            this.$message({message: '單價只能填寫數字和逗號!', type: 'warning'})
            return;
        }
        let totalPrice = (Number(this.addOtherValue.number) * Number(this.addOtherValue.unitPrice.replaceAll(',', ''))).toLocaleString();
        this.otherTable.push({
            specification: this.addOtherValue.specification,
            number: this.addOtherValue.number,
            unit: this.addOtherValue.unit,
            unitPrice: this.addOtherValue.unitPrice,
            price: totalPrice,
            remark: this.addOtherValue.remark,
        })
        this.otherDialogVisible = false;
        this.showModal=false
    },
    addOtherSelectChange(){
        let self = this;
        this.addOtherOption.forEach(function(item){
            if(item.name == self.addOtherValue.specification){
                self.addOtherValue.unitPrice = item.unitPrice;
            }
        })
    },
    clearOtherTable(){
        this.otherTable = [];
    },

  }
}
</script>