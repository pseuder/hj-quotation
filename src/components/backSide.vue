<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tab-body{
    height:80vh; 
    overflow:auto;
}
</style>

<template>
    <div>
        <div style="width: 90%; margin: auto auto">
            <el-tabs type="border-card" @tab-click="tabClick" v-model="tabsValue">
                <el-tab-pane label="設定" name="setting">
                    <span slot="label"><i class="el-icon-setting"></i> 設定</span>
                    <div class="tab-body">
                        <div style="margin: 30px;">
                            <el-button type="warning" style="font-size: 23px; width: 160px;" icon="el-icon-s-home"  @click="goMain">主頁面</el-button>
                        </div>
                        <div style="margin: 30px;">
                            <el-button type="danger" style="font-size: 23px; width: 160px;" icon="el-icon-switch-button"   @click="logOut">登出</el-button>
                        </div>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="帳號" name="account">
                    <div class="tab-body">
                        <el-table :data="userData" style="width: 100%; height:93%; overflow: auto">
                            <el-table-column label="帳號" prop="account">
                            </el-table-column>
                            <el-table-column label="密碼" prop="password">
                            </el-table-column>
                            <el-table-column label="操作" width="180">
                                <template slot-scope="scope">
                                    <el-button type="text" size="mini" @click="userEdit(scope.$index, scope.row)">編輯</el-button>
                                    <el-button type="text" size="mini" @click="userDelete(scope.$index, scope.row)">刪除</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-button style="position: absolute; right: 10px; bottom: 10px;" type="warning" @click="userAdd" circle icon="el-icon-plus"></el-button>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="商品" name="product">
                    <div class="tab-body">
                        <el-table :data="productData" style="width: 100%; height:93%; overflow: auto" :default-sort = "{prop: 'date', order: 'descending'}">
                            <el-table-column label="廠牌" prop="brand" sortable>
                            </el-table-column>
                            <el-table-column label="種類" prop="category" sortable>
                            </el-table-column>
                            <el-table-column label="名稱" prop="name" sortable>
                            </el-table-column>
                            <el-table-column label="單價" prop="unitPrice" sortable>
                            </el-table-column>
                            <el-table-column label="操作" width="180">
                                <template slot-scope="scope">
                                    <el-button type="text" size="mini" @click="productEdit(scope.$index, scope.row)">編輯</el-button>
                                    <el-button type="text" size="mini" @click="productDelete(scope.$index, scope.row)">刪除</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-button style="position: absolute; right: 10px; bottom: 10px;" type="warning" @click="productAdd" circle icon="el-icon-plus"></el-button>
                    </div>
                </el-tab-pane>
            </el-tabs>
        </div>

        <el-dialog title="修改帳號" :visible.sync="userDialogVisible" width="50%" :close-on-click-modal="false" :modal="false">
            <el-form :model="edituserData"  label-width="80px">
                <el-form-item label="帳號" prop="account">
                    <el-input v-model="edituserData.account" placeholder="請輸入帳號"></el-input>
                </el-form-item>
                <el-form-item label="密碼" prop="password">
                    <el-input v-model="edituserData.password" placeholder="請輸入密碼"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="userDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="userDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="修改商品" :visible.sync="productDialogVisible" width="50%" :close-on-click-modal="false" :modal="false">
            <el-form :model="editproductData"  label-width="80px">
                <el-form-item label="廠牌" prop="brand">
                    <el-input v-model="editproductData.brand" placeholder="請輸入廠牌"></el-input>
                </el-form-item>
                <el-form-item label="種類" prop="category">
                    <el-input v-model="editproductData.category" placeholder="請輸入種類"></el-input>
                </el-form-item>
                <el-form-item label="名稱" prop="name">
                    <el-input v-model="editproductData.name" placeholder="請輸入名稱"></el-input>
                </el-form-item>
                <el-form-item label="單價" prop="unitPrice">
                    <el-input v-model="editproductData.unitPrice" placeholder="請輸入單價"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="productDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="productDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="增加使用者" :visible.sync="userAddDialogVisible" width="50%" :close-on-click-modal="false" :modal="false">
            <el-form :model="adduserData"  label-width="80px">
                <el-form-item label="帳號" prop="account">
                    <el-input v-model="adduserData.account" placeholder="請輸入帳號"></el-input>
                </el-form-item>
                <el-form-item label="密碼" prop="password">
                    <el-input v-model="adduserData.password" placeholder="請輸入密碼"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="userAddDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="userAddDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="增加商品" :visible.sync="productAddDialogVisible" width="50%" :close-on-click-modal="false" :modal="false">
            <el-form :model="addproductData"  label-width="80px">
                <el-form-item label="廠牌" prop="brand">
                    <el-input v-model="addproductData.brand" placeholder="請輸入廠牌"></el-input>
                </el-form-item>
                <el-form-item label="種類" prop="category">
                    <el-input v-model="addproductData.category" placeholder="請輸入種類"></el-input>
                </el-form-item>
                <el-form-item label="名稱" prop="name">
                    <el-input v-model="addproductData.name" placeholder="請輸入名稱"></el-input>
                </el-form-item>
                <el-form-item label="單價" prop="unitPrice">
                    <el-input v-model="addproductData.unitPrice" placeholder="請輸入單價"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="productAddDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="productAddDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>
    </div>

</template>

<script>
export default {
  name: 'BackSide',
  data: function() {
    return { 
        tabsValue: 'account',
        userData: [],
        productData: [],
        userDialogVisible: false,
        edituserData:{
            id: '',
            account: '',
            password: '',
            index:'',
        },
        productDialogVisible: false,
        editproductData:{
            id: '',
            brand: '',
            category: '',
            name: '',
            unitPrice: '',
            index:'',
        },
        userAddDialogVisible: false,
        adduserData:{
            account: '',
            password: '',
        },
        productAddDialogVisible: false,
        addproductData:{
            brand: '',
            category: '',
            name: '',
            unitPrice: '',
        },
    }
  },
  created(){
        this.axios.get('getUser').then(res => {
            this.userData = res.data;
        })
  },
  methods:{
    tabClick(tab) {
        if(tab.label == '商品'){
            this.axios.get('getProduct').then(res => {
                this.productData = res.data;
            })
        }
    },
    userEdit(index, row){
        this.edituserData.id = row.id;
        this.edituserData.account = row.account
        this.edituserData.password = row.password
        this.edituserData.index = index;
        this.userDialogVisible = true
    },
    userDialogSubmit(){
        let self = this
        this.axios.post("/editUser",{
            edituserData : this.edituserData
        }).then(res => {
            self.userDialogVisible = false;
            self.userData[self.edituserData.index].account = self.edituserData.account
            self.userData[self.edituserData.index].password = self.edituserData.password
        })
    },
    userDelete(index, row){
        let self = this
        this.axios.post("/deleteUser",{
            id : row.id
        }).then(res => {
            self.userData.splice(index, 1)
        })
    },
    productEdit(index, row){
        this.editproductData.id = row.id;
        this.editproductData.brand = row.brand
        this.editproductData.category = row.category
        this.editproductData.name = row.name
        this.editproductData.unitPrice = row.unitPrice
        this.editproductData.index = index;
        this.productDialogVisible = true
    },
    productDialogSubmit(){
        let self = this
        this.axios.post("/editProduct",{
            editproductData : this.editproductData
        }).then(res => {
            self.productDialogVisible = false;
            self.productData[self.editproductData.index].brand = self.editproductData.brand
            self.productData[self.editproductData.index].category = self.editproductData.category
            self.productData[self.editproductData.index].name = self.editproductData.name
            self.productData[self.editproductData.index].unitPrice = self.editproductData.unitPrice
        })
    },
    productDelete(index, row){
        let self = this
        this.axios.post("/deleteProduct",{
            id : row.id
        }).then(res => {
            self.productData.splice(index, 1)
        })
    },
    userAdd(){
        this.userAddDialogVisible = true
    },
    userAddDialogSubmit(){
        let self = this
        this.axios.post("/addUser",{
            adduserData : this.adduserData
        }).then(res => {
            console.log(res.data)
            self.userData.push({
                id: res.data,
                account: self.adduserData.account,
                password: self.adduserData.password,
            })
            self.userAddDialogVisible = false;
        })
    },
    productAdd(){
        this.productAddDialogVisible = true
    },
    productAddDialogSubmit(){
        let self = this
        this.axios.post("/addProduct",{
            addproductData : this.addproductData
        }).then(res => {
            console.log(res.data)
            self.productData.push({
                id: res.data,
                brand: self.addproductData.brand,
                category: self.addproductData.category,
                name: self.addproductData.name,
                unitPrice: self.addproductData.unitPrice,
            })
            self.productAddDialogVisible = false;
        })
    },
    goMain(){
        this.$router.push('/main')
    },
    logOut(){
        sessionStorage.clear();
        this.$router.push('/login')
    },
  }
}
</script>