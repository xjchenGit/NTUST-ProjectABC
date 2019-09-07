import Taro,{Component} from '@tarojs/taro';
import {View,Text,Button} from '@tarojs/components';
//import {connect} from '@tarojs/redux';
import { AtTabBar } from 'taro-ui';
//import "~taro-ui/dist/style/components/tab-bar.scss";
//import "~taro-ui/dist/style/components/badge.scss";

class Menu extends Component{
    constructor () {
        super(...arguments)
        this.state = {
          current: 0
        }
      }
      handleClick (value) {
        this.setState({
          current: value
        })
      }

    render(){
        return (
            <AtTabBar
                fixed
                tabList={[
                    { title: '待办事项', iconType: 'bullet-list', text: 'new' },
                    { title: '拍照', iconType: 'camera' },
                    { title: '文件夹', iconType: 'folder', text: '100', max: '99' }
                ]}
                onClick={this.handleClick.bind(this)}
                current={this.state.current}
            />
        )
    }
}
export default Menu;