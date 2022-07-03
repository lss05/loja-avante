
/*Esta funcao valida integer para input text
function validarnumber(e,obj) {
    console.log(`o valor de event é: ${obj}`)
    var result = e.key >= 0? true : false
    if (result) {
        return true
    }
    return result
}
*/

function validarnumber(e,obj,totchar) {
    console.log(`o valor de event é: ${obj.value} é ${e.key}`)
    let cont = `${obj.value}${e.key}`
    console.log(typeof(cont))
    if (cont.length > totchar) {
        return false
    }
    var result = e.key >= 0? true : false
    if (result) {
        return true 
    }
    return result }