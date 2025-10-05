       
       <el-button>zhankai</el-button>

当点击zhankai按钮之后，向后台发送请求：
    const response = await axios.post('https://www.aworld.wiki/api/opinfo/get_oplist/', {
      op_type: 'm关注收藏',
      user_id: localStorage.getItem('userid') || '',
    });
这个请求是向后台调阅相关的操作记录，然后将返回的数据存储在oplist中，
然后根据这个组件上一层父组件传入的props参数与item_type的值进行对比判断，筛选相符的在页面中显示。

       <el-row>item_title</el-row>
       <el-row>类型：item_subtype
       <el-divider direction="vertical" />
       介绍：item_content
       </el-row>
       
       <el-pagination  
            v-if="oplist.length > 10"
            background
            @size-change="handleSizeChange"  
            @current-change="handleCurrentChange"  
            :current-page="currentPage"  
            :page-sizes="[10, 20, 30, 40]"  
            :page-size="pageSize"  
            layout="prev, pager, next"  
            :total="oplist.length">  
        </el-pagination>