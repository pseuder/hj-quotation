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

</style>

<style>

</style>

<template>
<div style="width: 90%; margin: auto auto">
    <div style="position:relative">
        <el-tabs type="border-card" v-model="tabsValue" >
            <el-tab-pane label="基本資料" name="basic">
                <div class="tab-body">
                    <el-form label-width="80px">
                        <div style="text-align: left; font-size: 28px;">店家</div>
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

                        
                        <div style="text-align: left; font-size: 28px;">客戶</div>
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
                    其他項目
                </div>
                <div class="tab-footer">
                    <el-button type="primary" @click="changeTab('service')" plain>上一步</el-button>
                    <el-button type="primary" @click="changeTab('finish')">下一步</el-button>
                </div>
            </el-tab-pane>
            <el-tab-pane label="完成" name="finish">
                <div class="tab-body">
                    <div :style="{'height':finishDivHeight, 'width':' 96%', 'max-width':' 675px', 'border':' black double 6px', 'margin':' auto'}">
                        <div style="height: 85%">
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
                            <div style="border-top: 1px solid #000; border-bottom: 1px solid #000; letter-spacing: 32px; text-align: center;" class="basic-info">
                                國際分離式變頻空調工程
                            </div>
                            <table border style="border-collapse:collapse; width:100%; font-family: PMingLiU;">
                                <tr style="">
                                    <th width="45%">空調設備規格</th>
                                    <th width="6%">數量</th>
                                    <th width="6%">單位</th>
                                    <th width="13%">單價</th>
                                    <th width="13%">金額</th>
                                    <th width="17%">備註</th>
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
                                <tr v-for="item of 10-serviceTable.length" :key="item">
                                    <td v-for="item of 6" :key="item" class="table-td"></td>
                                </tr>
                                <tr>
                                    <td class="toLeft table-td">施工日期:</td>
                                    <td v-for="item of 5" :key="item" class="table-td"></td>
                                </tr>
                                <tr>
                                    <td v-for="item of 6" :key="item" class="table-td"></td>
                                </tr>
                                <tr>
                                    <td colspan="6" class="toLeft table-td">
                                        <span style="margin-right: 15%;">訂金:</span>
                                        <span style="margin-right: 15%;">機器設備款:</span>
                                        <span>完成款:</span>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="letter-spacing: 32px; text-align:center" class="table-td">合計</td>
                                    <td colspan="5" style="text-align:center" class="table-td">${{allPrice}}</td>
                                </tr>
                            </table>
                        </div>
                        <div style="height: 150px">
                            <div style="" class="toLeft toFlex basic-info">
                                <div :style="{'line-height':finishSignLineHeight, 'width': '25%'}">和進電器水電行:</div>
                                <div style="width: 25%;"></div>
                                <div :style="{'line-height':finishSignLineHeight, 'width': '20%'}">客戶簽名:</div>
                                <div style="width: 30%;">
                                    <div v-if="clientSignImg==''" style="width: 100%; height: 98%;"  @click="signCanvasVisible=true" />
                                    <img v-else :src=clientSignImg style="width: 100%; height: 98%;" @click="signCanvasVisible=true" />
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
        <el-button type="primary" style="position:absolute; right:10px; top:40px; font-size: 23px;" icon="el-icon-setting" circle  @click="goBackSide"/>
    </div>
    
    <el-dialog title="選擇空調設備規格" :visible.sync="specificationDialogVisible" :close-on-click-modal="false" :modal="false">
        <div style="height: 55vh; overflow-y: auto; overflow-x: hidden;">
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
                    <el-input v-model="addSpecificationValue.unit" placeholder="輸入單位"></el-input>
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
            <el-button type="primary" plain @click="specificationDialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="addService">確 定</el-button>
        </span>
    </el-dialog>

    <el-dialog title="客戶簽名" :visible.sync="signCanvasVisible" :close-on-click-modal="false" width="80%" :modal="false">
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
                <el-button type="primary" plain @click="signCanvasVisible=false">取消</el-button>
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
        style="display: none;">
    >
    <section slot="pdf-content">
        <div :style="{'height':finishDivHeight, 'width':'750px', 'border':' black double 6px', 'margin':'20px 20px'}">
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
            <div style="border-top: 1px solid #000; border-bottom: 1px solid #000; letter-spacing: 32px; text-align: center;" class="basic-info">
                國際分離式變頻空調工程
            </div>
            <table border style="border-collapse:collapse; width:750px; font-family: PMingLiU;">
                <tr style="">
                    <th width="350px">空調設備規格</th>
                    <th width="40px">數量</th>
                    <th width="40px">單位</th>
                    <th width="100px">單價</th>
                    <th width="100px">金額</th>
                    <th width="120px">備註</th>
                </tr>
                <tr v-for="item in serviceTable" :key="item">
                    <td style="max-width: 365px; text-align:left;" class="table-td">{{item.specification}}</td>
                    <td style="max-width: 40px; text-align:center;" class="table-td">{{item.number}}</td>
                    <td style="max-width: 40px; text-align:center;" class="table-td">{{item.unit}}</td>
                    <td style="max-width: 100px; text-align:right;" class="table-td">
                        <div style="margin-right: 4px;">${{item.unitPrice}}</div>
                    </td>
                    <td style="max-width: 100px; text-align:right;" class="table-td">
                        <div style="margin-right: 4px;">${{item.price}}</div>
                    </td>
                    <td style="max-width: 165px; text-align:center;" class="table-td">{{item.remark}}</td>
                </tr>
                <tr v-for="item of 10-serviceTable.length" :key="item">
                    <td v-for="item of 6" :key="item" class="table-td"></td>
                </tr>
                <tr>
                    <td class="toLeft table-td">施工日期:</td>
                    <td v-for="item of 5" :key="item" class="table-td"></td>
                </tr>
                <tr>
                    <td v-for="item of 6" :key="item" class="table-td"></td>
                </tr>
                <tr>
                    <td colspan="6" class="toLeft table-td">
                        <span style="margin-right: 200px;">訂金:</span>
                        <span style="margin-right: 200px;">機器設備款:</span>
                        <span>完成款:</span>
                    </td>
                </tr>
                <tr>
                    <td style="letter-spacing: 32px; text-align:center" class="table-td">合計</td>
                    <td colspan="5" style="text-align:center" class="table-td">${{allPrice}}</td>
                </tr>
            </table>
            <div style="" class="toLeft toFlex basic-info">
                <div style="line-height: 145px; width: 400px;">和進電器水電行:</div>
                <div style="line-height: 145px;" class="toFlex">
                    <div>客戶簽名:</div>
                    <div v-if="clientSignImg==''" style="width: 275px; height: 80%;"  @click="signCanvasVisible=true" />
                    <img v-else :src=clientSignImg style="width: 275px; height: 80%;" @click="signCanvasVisible=true" />
                </div>
            </div>
        </div>
    </section>
    </vue-html2pdf>

    
        
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
            finishDivHeight: '1000px',
            finishSignLineHeight: '150px',
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
            allProduct:[],
            clientSignImg: '',
            signCanvasVisible: false,

            name: 'Vue.js',
            showLayout: false,
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
        this.clientForm.date = new Date();

        let ua = navigator.userAgent;
        let Agents = ["Android", "iPhone",
            "SymbianOS", "Windows Phone",
            "iPad", "iPod"];

        if (ua.indexOf("iPad") > 0) {
            this.finishDivHeight = '1050px';
        }
        else if (ua.indexOf("iPhone") > 0) {
            this.finishDivHeight = '1050px';
            this.finishSignLineHeight = '85px';
        }
        else if (ua.indexOf("SymbianOS") > 0) {
        }
        else if (ua.indexOf("Windows Phone") > 0) {
        }
        else if (ua.indexOf("Android") > 0) {
        }
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
        return this.serviceTable.reduce((total, item)=>{
            return (Number(String(total).replaceAll(',', ''))+Number(String(item.price).replaceAll(',', ''))).toLocaleString()
        }, 0);
    }
  },
  methods:{
    changeTab(destination){
        this.tabsValue = destination
    },
    deleteService(index, row){
        this.serviceTable.splice(index, 1)
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
    },
    addService(){
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
  }
}
</script>