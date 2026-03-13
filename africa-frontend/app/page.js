"use client"

import { useState } from "react"

export default function Home() {

  const [form,setForm]=useState({
    applicant_id:"",
    age:"",
    income:"",
    credit_score:"",
    existing_debt:"",
    loan_amount:"",
    employment_years:""
  })

  const [result,setResult]=useState(null)
  const [loading,setLoading]=useState(false)

  const handleChange=(e)=>{
    setForm({...form,[e.target.name]:e.target.value})
  }

  const submit=async()=>{

    setLoading(true)

    const res=await fetch(
      process.env.NEXT_PUBLIC_API_URL + "/assess",
      {
        method:"POST",
        headers:{
          "Content-Type":"application/json"
        },
        body:JSON.stringify({
          applicant_id:form.applicant_id,
          age:Number(form.age),
          income:Number(form.income),
          credit_score:Number(form.credit_score),
          existing_debt:Number(form.existing_debt),
          loan_amount:Number(form.loan_amount),
          employment_years:Number(form.employment_years)
        })
      }
    )

    const data=await res.json()

    setResult(data)
    setLoading(false)
  }

  return (
    <div style={{padding:"40px",fontFamily:"sans-serif"}}>

      <h1>AFRICA Credit Risk Test UI</h1>

      <div style={{display:"grid",gap:"10px",maxWidth:"400px"}}>

        <input name="applicant_id" placeholder="Applicant ID" onChange={handleChange}/>
        <input name="age" placeholder="Age" onChange={handleChange}/>
        <input name="income" placeholder="Income" onChange={handleChange}/>
        <input name="credit_score" placeholder="Credit Score" onChange={handleChange}/>
        <input name="existing_debt" placeholder="Existing Debt" onChange={handleChange}/>
        <input name="loan_amount" placeholder="Loan Amount" onChange={handleChange}/>
        <input name="employment_years" placeholder="Employment Years" onChange={handleChange}/>

        <button onClick={submit}>
          {loading ? "Processing..." : "Assess Risk"}
        </button>

      </div>

      {result && (

        <div style={{marginTop:"30px"}}>

          <h2>Decision</h2>

          <p><b>Decision:</b> {result.decision}</p>
          <p><b>Explanation:</b> {result.explanation}</p>
          <p><b>Confidence:</b> {result.llm_confidence}</p>

        </div>

      )}

    </div>
  )
}
     