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
    height: 50px; 
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

<template>
<div style="width: 80%; margin: auto auto">
    <el-tabs type="border-card" v-model="tabsValue">
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
                        <el-input v-model="companyForm.tax"></el-input>
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
                        <el-input v-model="clientForm.tax"></el-input>
                    </el-form-item>
                    <el-form-item label="客戶信箱">
                        <el-input v-model="clientForm.email"></el-input>
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
                    <el-table-column label="空調設備規格" prop="specification"></el-table-column>
                    <el-table-column label="數量" prop="number"></el-table-column>
                    <el-table-column label="單位" prop="unit"></el-table-column>
                    <el-table-column label="單價" prop="unitPrice"></el-table-column>
                    <el-table-column label="金額" prop="price"></el-table-column>
                    <el-table-column label="備註" prop="remark"></el-table-column>
                </el-table>
                <el-button type="warning" icon="el-icon-plus" circle @click="dialogFormVisible=true"></el-button>
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
                <vue-html2pdf
                    :show-layout="true"
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

                    @progress="onProgress($event)"
                    @hasStartedGeneration="hasStartedGeneration()"
                    @hasGenerated="hasGenerated($event)"
                    ref="html2Pdf"
                >
                <section slot="pdf-content">
                    <div style="height: 1070px; width: 750px; border: black double 6px; margin: 20px 20px;">
                        <div style="" class="basic-info">
                            <div style="text-align:center; font-size: 35px;">報   價   單</div>
                            <div style="" class="toLeft">和進電器水電行</div>
                            <div style="" class="toLeft">新竹縣新豐鄉建興路一段154-8號</div>
                            <div style="" class="toFlex">
                                <div style="">TEL：03-5576567</div>
                                <div style="margin-left:20px">FAX：03-573526</div>
                            </div>
                            <br>
                            <div style="" class="toFlex">
                                <div style="width:60%" class="toLeft">客戶名稱：馬先生</div>
                                <div style="" class="toLeft">日期：111/2/21</div>
                            </div>
                            <div style="" class="toFlex">
                                <div style="width:60%" class="toLeft">聯絡電話：0978-815281</div>
                                <div style="" class="toLeft">傳真：</div>
                            </div>
                            <div style="" class="toLeft">地址：新竹縣新豐鄉建興路一段154-8號</div>
                            <div style="" class="toLeft">Email：</div>
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
                            <tr v-for="item in testarr" :key="item">
                                <td style="max-width: 365px; text-align:left;" class="table-td">{{item.name}}</td>
                                <td style="max-width: 40px; text-align:center;" class="table-td">{{item.address}}</td>
                                <td style="max-width: 40px; text-align:center;" class="table-td">{{item.telephone}}</td>
                                <td style="max-width: 100px; text-align:right;" class="table-td">
                                    <div style="margin-right: 4px;">${{item.tax}}</div>
                                </td>
                                <td style="max-width: 100px; text-align:right;" class="table-td">
                                    <div style="margin-right: 4px;">${{item.email}}</div>
                                </td>
                                <td style="max-width: 165px; text-align:center;" class="table-td">${{item.note}}</td>
                            </tr>
                            <tr v-for="item of 10-testarr.length" :key="item">
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
                                <td colspan="5" style="text-align:center" class="table-td">$112345</td>
                            </tr>
                        </table>
                        <div style="height: 90px;" class="toLeft toFlex basic-info">
                            <div style="width: 400px; line-height: 90px; ">和進電器水電行:</div>
                            <div style="line-height: 90px;" class="toFlex">
                                <div>客戶簽名:</div>
                                <div v-if="clientSignImg==''" style="width: 275px; height: 80px;"  @click="signCanvasVisible=true" />
                                <img v-else :src=clientSignImg style="width: 275px; height: 80px;" @click="signCanvasVisible=true" />
                            </div>
                        </div>
                    </div>
                </section>
                </vue-html2pdf>
            </div>
            <div class="tab-footer">
                <el-button type="primary" @click="changeTab('other')" plain>上一步</el-button>
                <el-button type="primary" @click="generateReport">下載成PDF</el-button>
            </div>
        </el-tab-pane>
    </el-tabs>

    <el-dialog title="選擇空調設備規格" :visible.sync="dialogFormVisible">
        <div>
            <el-form :model="addSpecificationForm" label-width="80px">
                <el-form-item label="品牌">
                    <el-select v-model="addSpecificationValue.brand" placeholder="選擇品牌">
                        <el-option
                            v-for="item in addSpecificationOption.brand"
                            :key="item"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="種類">
                    <el-select v-model="addSpecificationValue.category" placeholder="選擇種類">
                        <el-option
                            v-for="item in addSpecificationOption.category"
                            :key="item"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="商品">
                    <el-select v-model="addSpecificationValue.product" placeholder="選擇商品">
                        <el-option
                            v-for="item in addSpecificationOption.product"
                            :key="item"
                            :label="item"
                            :value="item">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="數量">
                    <el-input v-model="addSpecificationValue.number" placeholder=""></el-input>
                </el-form-item>
                <el-form-item label="單位">
                    <el-input v-model="addSpecificationValue.unit" placeholder=""></el-input>
                </el-form-item>
                <el-form-item label="單價">
                    <el-input v-model="addSpecificationValue.unitPrice" placeholder=""></el-input>
                </el-form-item>
                <el-form-item label="備註">
                    <el-input v-model="addSpecificationValue.remark" placeholder=""></el-input>
                </el-form-item>
            </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="addService">確 定</el-button>
        </span>
    </el-dialog>

    <el-dialog title="客戶簽名" :visible.sync="signCanvasVisible" :close-on-click-modal="false">
        <vue-esign 
            ref="esign" 
            :width="800" 
            :height="300" 
            :isCrop="isCrop" 
            :lineWidth="lineWidth" 
            :lineColor="lineColor" 
            :bgColor.sync="bgColor"
            style="borderStyle: double; borderColor: black;"
        />
        <div style="margin-top:20px; text-align:right">
            <el-button type="primary" @click="$refs.esign.reset()">清除</el-button>
            <el-button type="primary" @click="signCanvasVisible=false">取消</el-button>
            <el-button type="primary" @click="handleGenerate">確定</el-button>
        </div>
    </el-dialog>

    
        
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
                tax:'03-573526',
            },
            clientForm:{
                company:'',
                address:'',
                telephone:'',
                tax:'',
                email:'',
            },
            serviceTable:[],
            dialogFormVisible: false,
            addSpecificationOption:{
                brand:['國際','日立'],
                category:['變頻冷專冷氣', '變頻冷專冷暖'],
                product:['CS-LJ71BA2/CU-LJ71BCA2', 'RA-25HV1'],
            },
            addSpecificationValue:{
                brand:'國際',
                category:'變頻冷專冷氣',
                product:' CS-LJ71BA2/CU-LJ71BCA2',
                number:'',
                unit:'',
                unitPrice:'',
                remark:'',
            },
            testarr:[
                {
                    name:'國際變頻冷專冷氣CS-LJ71BA2/CU-LJ71BCA2',
                    address:'1',
                    telephone:'組',
                    tax:'56000',
                    email:'56000',
                    note:'test1test1',
                },
                {
                    name:'日立變頻冷專冷暖RA-25HV1',
                    address:'1',
                    telephone:'米',
                    tax:'31000',
                    email:'31000',
                    note:'test2test2',
                },
            ],
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
  },
  computed: {
    htmlToPdfOptions() {
      return {
        margin: 0,

        filename: "我是pdf.pdf",

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
  },
  methods:{
    changeTab(destination){
    this.tabsValue = destination
    },
    addService(){
        let fullSpecification = this.addSpecificationValue.brand + this.addSpecificationValue.category + this.addSpecificationValue.product;
        this.serviceTable.push({
            specification: fullSpecification,
            number: this.addSpecificationValue.number,
            unit: this.addSpecificationValue.unit,
            unitPrice: this.addSpecificationValue.unitPrice,
            price: this.addSpecificationValue.number * this.addSpecificationValue.unitPrice,
            remark: this.addSpecificationValue.remark,
        })
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

    show: function(){
      this.showLayout = !this.showLayout
    },
    greet: function (event) {
      // `this` inside methods points to the Vue instance
      alert('Hello ' + this.name + '!')
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName)
      }
    },
    generateReport () {
      this.$refs.html2Pdf.generatePdf()
    }
  }
}
</script>