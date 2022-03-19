<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title{
    text-align:center; 
    font-size:30px;
}
.caption{
    text-align:left; 
    font-size:20px;
}
.input{
    width:100%;
    border-color:black;
}
.button{
    font-size:30px;
    width:100%;
    background-color:#439EFF;
    color:black;
}
.src{
    border: none;
    color: black;
    background-color: white;
    cursor: pointer;
    text-decoration:underline;
    font-size:20px;
}

</style>

<template>
  <div style="margin: auto auto">
    <el-card style="margin:100px auto; width:90%; max-width:500px;">
        <div style="margin:0 auto; width:90%; font-size:20px">
            <br><br>
            <div class="title">登入</div><br><br>
            <div class="caption">帳號</div>
            <el-input class="input" v-model="account" placeholder="請輸入帳號"></el-input><br><br>
            <div class="caption">密碼</div>
            <el-input class="input" v-model="password" placeholder="請輸入密碼" show-password></el-input><br><br><br>
            <el-button class="button"  plain @click="login">Log in</el-button><br><br>
            <br>
           
        </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'login',
  data: function() {
    return { 
        account:'',
        password:'',
    }
  },
  created(){
    this.$router.replace({query: ''}).catch(()=>{});
  },
  mounted() {//監聽enter 若按enter則觸發login
    let _this = this;
    document.onkeydown = function(e) {
        if (_this.$route.name == "login") {
            let key = window.event.keyCode;
            if (key == 13) 
                _this.login();
            }
    }
    
  },
  methods:{
    login(){
        let self = this;
        this.axios.get("/login",{
            params:{
                account:this.account,
                password:this.password
            }
        }).then(function(response){

            if(response.data == 'success'){
                sessionStorage.setItem("login", "true");//登入狀態
                self.$router.push({name: 'main'});
            }
            else
                self.$message({message: '登入失敗!', type: 'error'});
        });
    },
  }
}
</script>