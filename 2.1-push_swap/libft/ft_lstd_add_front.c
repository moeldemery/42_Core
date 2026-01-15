/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 15:35:47 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/09 15:35:50 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstd_add_front(td_list **lst, td_list *new)
{
	if (lst == NULL || new == NULL)
		return ;
	new->next = *lst;
	new->prev = NULL;
	if (*lst != NULL)
		(*lst)->prev = new;
	*lst = new;
}
