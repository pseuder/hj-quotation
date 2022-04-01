<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tab-body{
    height:80vh; 
    overflow:auto;
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
</style>

<template>
    <div>
        <div style="width: 90%; margin: auto auto">
            <div  v-if="showModal" class="myModal"></div>
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
                        <el-table :data="userData" style="width: 100%; height:93%; overflow: auto" v-loading="userTableLoading" empty-text="尚無資料">
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
                        <el-table 
                            :data="productData" 
                            style="width: 100%; height:93%; overflow: auto" 
                            :default-sort = "{prop: 'date', order: 'descending'}" 
                            v-loading="productTableLoading"
                            empty-text="尚無資料">
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
                <el-tab-pane label="其他" name="other">
                    <div class="tab-body">
                        <el-table 
                            :data="otherData" 
                            style="width: 100%; height:93%; overflow: auto" 
                            :default-sort = "{prop: 'date', order: 'descending'}" 
                            v-loading="otherTableLoading"
                            empty-text="尚無資料">
                            <el-table-column label="名稱" prop="name" sortable>
                            </el-table-column>
                            <el-table-column label="單價" prop="unitPrice" sortable>
                            </el-table-column>
                            <el-table-column label="操作" width="180">
                                <template slot-scope="scope">
                                    <el-button type="text" size="mini" @click="otherEdit(scope.$index, scope.row)">編輯</el-button>
                                    <el-button type="text" size="mini" @click="otherDelete(scope.$index, scope.row)">刪除</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-button style="position: absolute; right: 10px; bottom: 10px;" type="warning" @click="otherAdd" circle icon="el-icon-plus"></el-button>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="單位" name="unit">
                    <div class="tab-body">
                        <el-table 
                            :data="unitData" 
                            style="width: 100%; height:93%; overflow: auto"
                            v-loading="unitTableLoading"
                            empty-text="尚無資料">
                            <el-table-column label="名稱" prop="name">
                            </el-table-column>
                            <el-table-column label="操作" width="180">
                                <template slot-scope="scope">
                                    <el-button type="text" size="mini" @click="unitDelete(scope.$index, scope.row)">刪除</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-button style="position: absolute; right: 10px; bottom: 10px;" type="warning" @click="unitAdd" circle icon="el-icon-plus"></el-button>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="附件" name="attachment">
                    <div class="tab-body">
                        <el-table 
                            :data="attachmentData" 
                            style="width: 100%; height:93%; overflow: auto"
                            v-loading="attachmentTableLoading"
                            empty-text="尚無資料">
                            <el-table-column label="名稱" prop="name">
                            </el-table-column>
                            <el-table-column label="備註" prop="remark">
                            </el-table-column>
                            <el-table-column label="操作" width="180">
                                <template slot-scope="scope">
                                    <el-button type="text" size="mini" @click="attachmentEdit(scope.$index, scope.row)">編輯</el-button>
                                    <el-button type="text" size="mini" @click="attachmentDelete(scope.$index, scope.row)">刪除</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                        <el-button style="position: absolute; right: 10px; bottom: 10px;" type="warning" @click="attachmentAdd" circle icon="el-icon-plus"></el-button>
                    </div>
                </el-tab-pane>
            </el-tabs>
        </div>

        <el-dialog title="修改帳號" :visible.sync="userDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="edituserData"  label-width="80px">
                <el-form-item label="帳號" prop="account">
                    <el-input v-model="edituserData.account" placeholder="請輸入帳號"></el-input>
                </el-form-item>
                <el-form-item label="密碼" prop="password">
                    <el-input v-model="edituserData.password" placeholder="請輸入密碼"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="userDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="userDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="修改商品" :visible.sync="productDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
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
                <el-button @click="productDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="productDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="修改其他" :visible.sync="otherDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="editotherData"  label-width="80px">
                <el-form-item label="名稱" prop="name">
                    <el-input v-model="editotherData.name" placeholder="請輸入名稱"></el-input>
                </el-form-item>
                <el-form-item label="單價" prop="unitPrice">
                    <el-input v-model="editotherData.unitPrice" placeholder="請輸入單價"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="otherDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="otherDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="增加使用者" :visible.sync="userAddDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="adduserData"  label-width="80px">
                <el-form-item label="帳號" prop="account">
                    <el-input v-model="adduserData.account" placeholder="請輸入帳號"></el-input>
                </el-form-item>
                <el-form-item label="密碼" prop="password">
                    <el-input v-model="adduserData.password" placeholder="請輸入密碼"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="userAddDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="userAddDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="增加商品" :visible.sync="productAddDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="addproductData"  label-width="80px">
                <el-form-item label="品牌" prop="brand">
                    <el-input v-model="addproductData.brand" placeholder="請輸入品牌"></el-input>
                </el-form-item>
                <el-form-item label="種類" prop="category">
                    <el-input v-model="addproductData.category" placeholder="請輸入種類"></el-input>
                </el-form-item>
                <el-form-item label="商品" prop="name">
                    <el-input v-model="addproductData.name" placeholder="請輸入商品"></el-input>
                </el-form-item>
                <el-form-item label="單價" prop="unitPrice">
                    <el-input v-model="addproductData.unitPrice" placeholder="請輸入單價"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="productAddDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="productAddDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="增加其他" :visible.sync="otherAddDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="addotherData"  label-width="80px">
                <el-form-item label="名稱" prop="name">
                    <el-input v-model="addotherData.name" placeholder="請輸入名稱"></el-input>
                </el-form-item>
                <el-form-item label="單價" prop="unitPrice">
                    <el-input v-model="addotherData.unitPrice" placeholder="請輸入單價"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="otherAddDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="otherAddDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="增加單位" :visible.sync="unitAddDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="addunitData"  label-width="80px">
                <el-form-item label="單位" prop="name">
                    <el-input v-model="addunitData.name" placeholder="請輸入單位"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="unitAddDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="unitAddDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="增加附件" :visible.sync="attachmentAddDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="addattachmentData"  label-width="80px">
                <el-form-item label="附件名稱" prop="name">
                    <el-input v-model="addattachmentData.name" placeholder="請輸入附件名稱"></el-input>
                </el-form-item>
                <el-form-item label="附件備註" prop="remark">
                    <el-input v-model="addattachmentData.remark" placeholder="請輸入附件備註"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="attachmentAddDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="attachmentAddDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="修改附件" :visible.sync="attachmentDialogVisible" width="50%" :close-on-click-modal="false" :modal="false" :close-on-press-escape="false" :show-close="false">
            <el-form :model="editattachmentData"  label-width="80px">
                <el-form-item label="附件名稱" prop="name">
                    <el-input v-model="editattachmentData.name" placeholder="請輸入附件名稱"></el-input>
                </el-form-item>
                <el-form-item label="附件備註" prop="remark">
                    <el-input v-model="editattachmentData.remark" placeholder="請輸入附件備註"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="attachmentDialogVisible = false; showModal = false">取 消</el-button>
                <el-button type="primary" @click="attachmentDialogSubmit">確 定</el-button>
            </div>
        </el-dialog>
    </div>

</template>

<script>
export default {
  name: 'BackSide',
  data: function() {
    return { 
        showModal: false,
        tabsValue: 'account',
        userData: [],
        productData: [],
        otherData:[],
        unitData:[],
        attachmentData:[],
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
        otherDialogVisible: false,
        editotherData:{
            id: '',
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
        otherAddDialogVisible: false,
        addotherData:{
            name: '',
            unitPrice: '',
        },
        unitAddDialogVisible: false,
        addunitData:{
            name: ''
        },
        addattachmentData:{
            name: '',
            remark: '',
        },
        editattachmentData:{
            id: '',
            name: '',
            remark: '',
            index:'',
        },
        userTableLoading: false,
        productTableLoading: false,
        otherTableLoading: false,
        unitTableLoading: false,
        attachmentTableLoading: false,
        
        
    }
  },
  created(){
        let self = this;
        this.userTableLoading = true;
        this.axios.get('getUser').then(res => {
            self.userData = res.data;
            self.userTableLoading = false
        })
  },
  methods:{
    tabClick(tab) {
        let self = this;
        if(tab.label == '帳號'){
            self.userTableLoading = true;
            this.axios.get('getUser').then(res => {
                self.userData = res.data;
                self.userTableLoading = false
            })
        }
        else if(tab.label == '商品'){
            self.productTableLoading = true;
            this.axios.get('getProduct').then(res => {
                self.productData = res.data;
                self.productTableLoading = false
            })
        }
        else if(tab.label == '其他'){
            self.otherTableLoading = true;
            this.axios.get('getOther').then(res => {
                self.otherData = res.data;
                self.otherTableLoading = false
            })
        }
        else if(tab.label == '單位'){
            self.unitTableLoading = true;
            this.axios.get('getUnit').then(res => {
                self.unitData = res.data;
                self.unitTableLoading = false
            })
        }
        else if(tab.label == '附件'){
            self.attachmentTableLoading = true;
            this.axios.get('getAttachment').then(res => {
                self.attachmentData = res.data;
                self.attachmentTableLoading = false
            })
        }
    },
    userEdit(index, row){
        this.edituserData.id = row.id;
        this.edituserData.account = row.account
        this.edituserData.password = row.password
        this.edituserData.index = index;
        this.userDialogVisible = true
        this.showModal = true
    },
    userDialogSubmit(){
        let self = this
        this.axios.post("/editUser",{
            edituserData : this.edituserData
        }).then(res => {
            self.userDialogVisible = false;
            this.showModal = false
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
        this.showModal = true
    },
    productDialogSubmit(){
        //只能填寫數字和逗號
        if(!this.editproductData.unitPrice.match(/^[0-9,]*$/)){
            this.$message({message: '單價只能填寫數字和逗號!', type: 'warning'})
            return;
        }
        let self = this
        this.axios.post("/editProduct",{
            editproductData : this.editproductData
        }).then(res => {
            self.productDialogVisible = false;
            self.showModal = false
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
    otherEdit(index, row){
        this.editotherData.id = row.id;
        this.editotherData.name = row.name
        this.editotherData.unitPrice = row.unitPrice
        this.editotherData.index = index;
        this.otherDialogVisible = true
        this.showModal = true
    },
    otherDialogSubmit(){
        //只能填寫數字和逗號
        if(!this.editotherData.unitPrice.match(/^[0-9,]*$/)){
            this.$message({message: '單價只能填寫數字和逗號!', type: 'warning'})
            return;
        }
        let self = this
        this.axios.post("/editOther",{
            editotherData : this.editotherData
        }).then(res => {
            self.otherDialogVisible = false;
            self.showModal = false
            self.otherData[self.editotherData.index].name = self.editotherData.name
            self.otherData[self.editotherData.index].unitPrice = self.editotherData.unitPrice
        })
    },
    otherDelete(index, row){
        let self = this
        this.axios.post("/deleteOther",{
            id : row.id
        }).then(res => {
            self.otherData.splice(index, 1)
        })
    },
    otherAddDialogSubmit(){
        //只能填寫數字和逗號
        if(!this.addotherData.unitPrice.match(/^[0-9,]*$/)){
            this.$message({message: '單價只能填寫數字和逗號!', type: 'warning'})
            return;
        }
        let self = this
        this.axios.post("/addOther",{
            addotherData : this.addotherData
        }).then(res => {
            self.otherData.push({
                id: res.data,
                name: self.addotherData.name,
                unitPrice: self.addotherData.unitPrice,
            })
            self.addotherData.name = ''
            self.addotherData.unitPrice = ''
            self.otherAddDialogVisible = false;
            self.showModal = false
        })
    },
    otherAdd(){
        this.otherAddDialogVisible = true
        this.showModal = true
    },
    userAdd(){
        this.userAddDialogVisible = true
        this.showModal = true
    },
    userAddDialogSubmit(){
        let self = this
        this.axios.post("/addUser",{
            adduserData : this.adduserData
        }).then(res => {
            self.userData.push({
                id: res.data,
                account: self.adduserData.account,
                password: self.adduserData.password,
            })
            self.adduserData.account = ''
            self.adduserData.password = ''
            self.userAddDialogVisible = false;
            self.showModal = false
        })
    },
    productAdd(){
        this.productAddDialogVisible = true
        this.showModal = true
    },
    productAddDialogSubmit(){
        //只能填寫數字和逗號
        if(!this.addproductData.unitPrice.match(/^[0-9,]*$/)){
            this.$message({message: '單價只能填寫數字和逗號!', type: 'warning'})
            return;
        }
        let self = this
        this.axios.post("/addProduct",{
            addproductData : this.addproductData
        }).then(res => {
            self.productData.push({
                id: res.data,
                brand: self.addproductData.brand,
                category: self.addproductData.category,
                name: self.addproductData.name,
                unitPrice: self.addproductData.unitPrice,
            })
            self.addproductData.brand = ''
            self.addproductData.category = ''
            self.addproductData.name = ''
            self.addproductData.unitPrice = ''
            self.productAddDialogVisible = false;
            self.showModal = false
        })
    },
    unitDelete(index, row){
        let self = this
        this.axios.post("/deleteUnit",{
            id : row.id
        }).then(res => {
            self.unitData.splice(index, 1)
        })
    },
    unitAdd(){
        this.unitAddDialogVisible = true
        this.showModal = true
    },
    unitAddDialogSubmit(){
        let self = this
        this.axios.post("/addUnit",{
            addunitData : this.addunitData
        }).then(res => {
            self.unitData.push({
                id: res.data,
                name: self.addunitData.name,
            })
            self.addunitData.name = ''
            self.unitAddDialogVisible = false;
            self.showModal = false
        })
    },
    attachmentEdit(index, row){
        this.editattachmentData.id = row.id;
        this.editattachmentData.name = row.name
        this.editattachmentData.remark = row.remark
        this.editattachmentData.index = index;
        this.attachmentDialogVisible = true
        this.showModal = true
    },
    attachmentDelete(index, row){
        let self = this
        this.axios.post("/deleteAttachment",{
            id : row.id
        }).then(res => {
            self.attachmentData.splice(index, 1)
        })
    },
    attachmentAdd(){
        this.attachmentAddDialogVisible = true
        this.showModal = true
    },
    attachmentAddDialogSubmit(){
        let self = this
        this.axios.post("/addAttachment",{
            addattachmentData : this.addattachmentData
        }).then(res => {
            self.attachmentData.push({
                id: res.data,
                name: self.addattachmentData.name,
                remark: self.addattachmentData.remark,
            })
            self.addattachmentData.name = ''
            self.addattachmentData.remark = ''
            self.attachmentAddDialogVisible = false;
            self.showModal = false
        })
    },
    attachmentDialogSubmit(){
        let self = this
        this.axios.post("/editAttachment",{
            editattachmentData : this.editattachmentData
        }).then(res => {
            self.attachmentDialogVisible = false;
            self.showModal = false
            self.attachmentData[self.editattachmentData.index].name = self.editattachmentData.name
            self.attachmentData[self.editattachmentData.index].remark = self.editattachmentData.remark
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