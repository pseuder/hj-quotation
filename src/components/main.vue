<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

<template>
<div style="width: 80%; margin: auto auto">
    <el-tabs type="border-card" v-model="tabsValue">
        <el-tab-pane label="基本資料" name="basic">
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

            <div style="margin-top:20px; text-align:right">
                <el-button type="primary" @click="changeTab('service')">下一步</el-button>
            </div>
            <el-button type="primary" @click="changeTab('service')">下一步</el-button>
        </el-tab-pane>
        <el-tab-pane label="服務項目" name="service">
            <el-table :data="serviceTable">
                <el-table-column label="空調設備規格" prop="specification"></el-table-column>
                <el-table-column label="數量" prop="number"></el-table-column>
                <el-table-column label="單位" prop="unit"></el-table-column>
                <el-table-column label="單價" prop="unitPrice"></el-table-column>
                <el-table-column label="金額" prop="price"></el-table-column>
                <el-table-column label="備註" prop="remark"></el-table-column>
            </el-table>
            <el-button type="warning" icon="el-icon-plus" circle @click="dialogFormVisible=true"></el-button>

            <div style="margin-top:20px; text-align:right">
                <el-button type="primary" @click="changeTab('basic')">上一步</el-button>
                <el-button type="primary" @click="changeTab('other')">下一步</el-button>
            </div>
        </el-tab-pane>
        <el-tab-pane label="其他項目" name="other">其他項目</el-tab-pane>
        <el-tab-pane label="完成">完成</el-tab-pane>
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
</template>

<script>
export default {
  name: 'Main',
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
            }
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
  }
}
</script>