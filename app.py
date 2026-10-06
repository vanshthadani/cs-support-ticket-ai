
import streamlit as st

from inference.classifier import classify_email


st.title("Customer Support AI")
st.write("Turn customer emails into structured support tickets.")


# Example emails
example_emails = {
    "Refund Pending": """Hi,

I returned my running shoes two weeks ago, but I still haven't received my refund. Could you please check the status?

Thanks.""",

    "Delivery Delayed": """Hello,

My order was supposed to arrive three days ago, but it still hasn't been delivered. The tracking hasn't updated either.

Can you please check what's happening with my package?""",

    "Damaged Product": """Hi,

My coffee machine arrived today, but the body is cracked and damaged. I can't use it in this condition.

I'd like a replacement, please.""",

    "Payment Failed": """Hello,

I've tried paying for my order several times, but every payment attempt keeps failing. My card works normally elsewhere.

Please help me complete the payment."""
}


st.subheader("Try an example")

selected_example = st.selectbox(
    "Choose a sample email",
    ["None"] + list(example_emails.keys())
)


# Put selected example into the text area
default_email = ""

if selected_example != "None":
    default_email = example_emails[selected_example]


email = st.text_area(
    "Customer support email",
    value=default_email,
    height=200,
    placeholder="Paste a customer support email here..."
)


if st.button("Analyze Email", type="primary"):

    if not email.strip():
        st.warning("Please enter a customer support email.")

    else:
        with st.spinner("Analyzing email..."):
            result = classify_email(email)

        st.divider()
        st.subheader("Support Ticket")

        # Ticket overview
        col1, col2, col3 = st.columns([1.5, 1.5, 1])

        with col1:
            st.write("**Category**")
            st.info(result["category"])

        with col2:
            st.write("**Subcategory**")
            st.info(result["subcategory"])

        with col3:
            st.write("**Urgency**")
            st.metric(
                label="",
                value=f'{result["urgency"]}/10'
            )

        st.divider()

        # Customer state
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("**Sentiment**")
            st.write(result["sentiment"])

        with col2:
            st.write("**Customer Satisfaction**")
            st.write(result["customer_satisfaction"])

        with col3:
            st.write("**Detected Product**")
            st.write(result["detected_product"] or "None")

        st.divider()

        # Issue
        st.write("**Issue**")
        st.info(result["issue"])

        # Action
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Requested Action**")
            st.write(result["requested_action"])

        with col2:
            st.write("**Requires Human**")
            if result["requires_human"]:
                st.error("Yes")
            else:
                st.success("No")
